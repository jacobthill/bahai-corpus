import glob, operator, os, re
from collections import Counter
from helper import build_corpus
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import numpy as np
import pandas as pd
import seaborn as sns

# # Gather all file names
corpus_dir = '/Users/jtim/Dropbox/Academic/sources/corpora/bahai-works/data/'
authors = ['bahaullah', 'bab', 'abdulbaha', 'shoghi-effendi']
languages = ['ar', 'fa']

file_names = build_corpus(corpus_dir, authors, languages)

# Functions containing the various steps of normalization
def process_one(text):
    return text

def process_two(text):
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("﴾", "")
    text = text.replace("﴿", "")
    text = text.replace('"', '')
    text = text.replace(":", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace(chr(46), " .") # period
    text = text.replace(chr(46), "") # period
    text = text.replace(chr(10), "") # period
    text = text.replace(chr(1548), " ,") # comma
    text = text.replace(chr(1548), "") # comma
    text = text.replace(chr(44), "") # comma
    text = text.replace(chr(10), "") # data link escape
    text = text.replace(chr(12), "") # formfeed
    text = text.replace(chr(8236), "") # pop directional formatting
    text = text.replace(chr(8235), "") # right-to-left embedding
    text = text.replace(chr(9), "") # character tabulation
    text = text.replace(chr(42), "") # asterisk
    text = text.replace(u'\u200c', ' ') # half space
    text = text.replace(u'\u200d', ' ') # zero width joiner
    text = text.replace(u'\u200f', '') # right-to-left mark
    text = text.apply(lambda s: s and re.sub('[^\w\s]', '', s)) # any other whitespace, number, etc.
    return text

def process_three(text):
    text = process_two(text)
    # replace all diacritics
    char = 1611
    for i in range(20):
        text = text.replace(chr(char), "") # decimal
        char += 1
    # normalize characters
    text = text.replace(chr(1600), "") # tatweel
    text = text.replace(chr(1705), chr(1603)) # kaf
    text = text.replace(chr(1609), chr(1610)) # ya
    text = text.replace(chr(1740), chr(1610)) # ya
    text = text.replace(chr(1574), chr(1610)) # ya
    text = text.strip("")
    return text

# A dictionary of functions
dispatcher = {'process_one': [process_one, 'one'],
              'process_two': [process_two, 'two'],
              'process_three': [process_three, 'three']}

# Main loop
def main():
    # Iterate through the functions in dispatcher and process the text with each
    for value in dispatcher.values():
        # Declare counter variables
        arabic_counter = Counter()
        persian_counter = Counter()
        combined_counter = Counter()

        # Declare vocabulary sets
        arabic_vocabulary = set()
        persian_vocabulary = set()

        # Declare color variables
        # light_blue = '#9fbfdf'
        blue = '#0077b3'
        # grey = '#d9e6f2'

        for name in file_names:
            if 'ar.txt' in name:
                with open(name, 'r') as f:
                    #### Error, use Counter instead of set? ####
                    words = set(value[0](f.read()).split(' '))
                    combined_counter.update(words)
                    arabic_counter.update(words)
                    arabic_vocabulary.update(words)
            else:
                with open(name, 'r') as f:
                    #### Error, use Counter instead of set? ####
                    words = set(value[0](f.read()).split(' '))
                    combined_counter.update(words)
                    persian_counter.update(words)
                    persian_vocabulary.update(words)

        directory = '/Users/jtim/Dropbox/Academic/research/dissertation/research/output/normalize/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        figures = '/Users/jtim/Dropbox/Academic/research/dissertation/research/output/figures/'
        if not os.path.exists(figures):
            os.makedirs(figures)

        with open('{}combined-{}.txt'.format(directory, value[1]), 'w') as out_file:
            # out_file.write('Processing: Split on white space, no character normalization.\n\n')
            out_file.write('Number of combined words: {}\n\n'.format(sum(combined_counter.values())))
            out_file.write('Total number of combined words: {}\n\n'.format(len(arabic_vocabulary.difference(persian_vocabulary)) + len(persian_vocabulary)))
            for word, count in combined_counter.most_common(1000):
                chars = [ord(_c) for _c in word]
                spaces = ' ' * (12 - len(chars))
                out_file.write("{}\n".format(word))
                out_file.write("Word count: {}{}u{}\n\n".format(count, spaces, chars))

        with open('{}arabic-{}.txt'.format(directory, value[1]), 'w') as out_file:
            # out_file.write('Processing: Split on white space, no character normalization.\n\n')
            out_file.write('Number of Arabic words: {}\n\n'.format(sum(arabic_counter.values())))
            out_file.write('Total number of arabic words: {}\n\n'.format(len(arabic_vocabulary)))
            for word, count in arabic_counter.most_common(1000):
                chars = [ord(_c) for _c in word]
                spaces = ' ' * (12 - len(chars))
                out_file.write("{}\n".format(word))
                out_file.write("Word count: {}{}u{}\n\n".format(count, spaces, chars))

        with open('{}persian-{}'.format(directory, value[1]), 'w') as out_file:
            # out_file.write('Processing: Split on white space, no character normalization.\n\n')
            out_file.write('Number of Persian words: {}\n\n'.format(sum(persian_counter.values())))
            out_file.write('Total number of persian words: {}\n\n'.format(len(persian_vocabulary)))
            for word, count in persian_counter.most_common(1000):
                chars = [ord(_c) for _c in word]
                spaces = ' ' * (12 - len(chars))
                out_file.write("{}\n".format(word))
                out_file.write("Word count: {}{}u{}\n\n".format(count, spaces, chars))

        # Load into dataframe for each processing step
        df = pd.DataFrame.from_dict(combined_counter, orient='index').reset_index()
        df = df.rename(columns={'index':'word', 0:'count'})
        df = df.sort_values('count', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
        df['word_rank'] = df['count'].rank(ascending=False)

        # Plot Zipf's law for each processing step
        f, ax = plt.subplots(figsize=(7, 7))
        ax.set(xscale="log", yscale="log")
        sns.regplot("count", "word_rank", df, ax=ax, scatter_kws={"s": 100})
        plt.savefig('{}combined-{}'.format(figures, value[1]))

        length_before_min = len(arabic_vocabulary) + len(persian_vocabulary)
        # Create list of minimumally occuring words from full set
        frequency = [5]
        for i in frequency: # Iterate through frequency and plot each processing step, frequency threshold
            for word, count in arabic_counter.items():
                if count < i:
                    try: # Need to avoid key error if i = 1
                        if i != 1:
                            arabic_vocabulary.remove(word)
                    except:
                        pass

            for word, count in persian_counter.items():
                if count < i:
                    try: # Need to avoid key error if i = 1
                        if i != 1:
                            persian_vocabulary.remove(word)
                    except:
                        pass

            length_after_min = len(arabic_vocabulary) + len(persian_vocabulary)
            print("The effect of the minimum frequency threshold on the total vocabulary with {}: {} - {} = {}".format(value, length_before_min, length_after_min, (length_before_min - length_after_min)))
            # Plot Venn diagram for each processing step and each frequecny threshold
            plt.figure(figsize=(6,4))
            v = venn2(subsets = (len(arabic_vocabulary.difference(persian_vocabulary)),
                                 len(persian_vocabulary.difference(arabic_vocabulary)),
                                 len(arabic_vocabulary.intersection(persian_vocabulary))), set_labels = ('Arabic', 'Persian'))
            v.get_patch_by_id('11').set_alpha(0.6) # overlap; third item in venn2 object
            v.get_patch_by_id('100').set_alpha(.5) # left circle; first item in venn2 object
            v.get_patch_by_id('10').set_alpha(1) # right circle; second item in venn2 object
            v.get_patch_by_id('11').set_color('white') # overlap; third item in venn2 object
            v.get_patch_by_id('100').set_color('white') # left circle; first item in venn2 object
            v.get_patch_by_id('010').set_color('grey') # right circle; second item in venn2 object
            c = venn2_circles(subsets = (len(arabic_vocabulary.difference(persian_vocabulary)),
                                         len(persian_vocabulary.difference(arabic_vocabulary)),
                                         len(arabic_vocabulary.intersection(persian_vocabulary))), linestyle='solid')
            # plt.title("Venn diagram: process={}, minimum frequency threshold={}".format(value[1], i))
            plt.savefig('{}venn-proc-{}-freq{}.png'.format(figures, value[1], i))

if __name__ == "__main__":
    main()
