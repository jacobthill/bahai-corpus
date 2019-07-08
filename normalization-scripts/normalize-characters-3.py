import glob, operator, os, re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Gather all file names
os.chdir('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/combined-corpus/')
file_names = glob.glob('*.txt')

# Contains all of the normalization logic
def normalize_carachters(text):
    char = 1611
    for i in range(20):
        text = text.replace(chr(char), "") # decimal
        char += 1
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("(", "")
    text = text.replace(")", "")
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
    text = text.replace(chr(12), "") # formfeed
    text = text.replace(chr(8236), "") # pop directional formatting
    text = text.replace(chr(8235), "") # right-to-left embedding
    text = text.replace(chr(12), "") # formfeed
    text = text.replace(chr(9), "") # character tabulation
    text = text.replace(chr(42), "") # asterisk
    text = text.replace(chr(1600), "") # tatweel
    text = text.replace(chr(1705), chr(1603)) # kaf
    text = text.replace(chr(1609), chr(1610)) # ya
    text = text.replace(chr(1740), chr(1610)) # ya
    text = text.replace(chr(1574), chr(1610)) # ya
    text = text.strip("")
    return text

# Main loop
def main():
    # Declare variables
    counter = Counter()
    total_number_of_words = 0

    for name in file_names:
        with open(name, 'r') as f:
            words = set(normalize_carachters(f.read()).split(' '))
            total_number_of_words += len(words)
            counter.update(words)

    with open('../../output/normalize-characters-3.txt', 'w') as out_file:
        out_file.write('Processing: Split on white space, no character normalization.\n\n')
        out_file.write('Number of words in vocabulary: {}\n\n'.format(len(counter)))
        out_file.write('Total number of words: {}\n\n'.format(total_number_of_words))
        for word, count in counter.most_common()[:-1000-1:-1]: # least common
        # for word, count in counter.most_common(1000):
            chars = [ord(_c) for _c in word]
            spaces = ' ' * (12 - len(chars))
            out_file.write("{}\n".format(word))
            out_file.write("Word count: {}{}u{}\n\n".format(count, spaces, chars))

    # # Load into dataframe
    # df = pd.DataFrame.from_dict(counter, orient='index').reset_index()
    # df = df.rename(columns={'index':'word', 0:'count'})
    # df = df.sort_values('count', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
    # df['word_rank'] = df['count'].rank(ascending=False)
    #
    # # Plot zip's law
    # f, ax = plt.subplots(figsize=(7, 7))
    # ax.set(xscale="log", yscale="log")
    # sns.regplot("count", "word_rank", df, ax=ax, scatter_kws={"s": 100})
    # plt.show()

    # Testing
    print(total_number_of_words == sum(counter.values()))

if __name__ == "__main__":
    main()
