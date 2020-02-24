from helper import build_corpus, process
from collections import Counter
import glob, os, random
import matplotlib.pyplot as plt
import numpy as np

arabic_islamicate_files = glob.glob('/Users/jtim/Dropbox/Academic/sources/corpora/cleaned-combined-open-arabic/*.txt')
print(len(arabic_islamicate_files))
persian_islamicate_files = glob.glob('/Users/jtim/Dropbox/Academic/sources/corpora/cleaned-persian-dh/*.txt')
print(len(persian_islamicate_files))

authors = ['abdulbaha', 'bab', 'bahaullah', 'shoghi-effendi']
arabic_bahai_files = build_corpus('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/', authors, ['ar'])
persian_bahai_files = build_corpus('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/', authors, ['fa'])

def main():
    directory = '/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/output/islamicate-texts/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Islamicate variables
    arabic_islamicate_counter = Counter()
    persian_islamicate_counter = Counter()
    arabic_islamicate_vocabulary = set()
    persian_islamicate_vocabulary = set()
    arabic_islamicate_word_count = 0
    persian_islamicate_word_count = 0
    arabic_islamicate_vocabularies = []
    persian_islamicate_vocabularies = []

    # Baha'i variables
    arabic_bahai_counter = Counter()
    persian_bahai_counter = Counter()
    arabic_bahai_vocabulary = set()
    persian_bahai_vocabulary = set()
    arabic_bahai_word_count = 0
    persian_bahai_word_count = 0
    arabic_bahai_vocabularies = []
    persian_bahai_vocabularies = []

    # Process Islamicate files
    for a_file in arabic_islamicate_files:
        with open(a_file, 'r') as af:
            words = Counter(process(af.read()).split())
            arabic_islamicate_word_count += len(words)
            arabic_islamicate_vocabulary.update(words)
            arabic_islamicate_counter.update(words)

    for p_file in persian_islamicate_files:
        with open(p_file, 'r') as pf:
            words = Counter(process(pf.read()).split())
            persian_islamicate_word_count += len(words)
            persian_islamicate_vocabulary.update(words)
            persian_islamicate_counter.update(words)

    # Process Baha'i files
    for a_file in arabic_bahai_files:
        with open(a_file, 'r') as af:
            words = Counter(process(af.read()).split())
            arabic_bahai_word_count += len(words)
            arabic_bahai_vocabulary.update(words)
            arabic_bahai_counter.update(words)

    for p_file in persian_bahai_files:
        with open(p_file, 'r') as pf:
            words = Counter(process(pf.read()).split())
            persian_bahai_word_count += len(words)
            persian_bahai_vocabulary.update(words)
            persian_bahai_counter.update(words)

    # Common variables
    minimum_threshold = 5
    for i in range(1, minimum_threshold):
        # remove minimum_threshold number of words
        for item in arabic_islamicate_counter.items():
            if item[1] <= i:
                if item[0] in arabic_islamicate_vocabulary:
                    arabic_islamicate_vocabulary.remove(item[0])

        for item in persian_islamicate_counter.items():
            if item[1] <= i:
                if item[0] in persian_islamicate_vocabulary:
                    persian_islamicate_vocabulary.remove(item[0])

        for item in arabic_bahai_counter.items():
            if item[1] <= i:
                if item[0] in arabic_bahai_vocabulary:
                    arabic_bahai_vocabulary.remove(item[0])

        for item in persian_bahai_counter.items():
            if item[1] <= i:
                if item[0] in persian_bahai_vocabulary:
                    persian_bahai_vocabulary.remove(item[0])

    combined_bahai_counter = arabic_bahai_counter + persian_bahai_counter
    bahai_intersection = persian_bahai_vocabulary.intersection(arabic_bahai_vocabulary)
    islamicate_intersection = persian_islamicate_vocabulary.intersection(arabic_islamicate_vocabulary)


    # Print Islamicate stats
    print("Islamicate language statistics:")
    print("Arabic word count: {}".format(arabic_islamicate_word_count))
    print("Persian word count: {}".format(persian_islamicate_word_count))
    print("Arabic vocabulary: {}".format(len(arabic_islamicate_vocabulary)))
    print("Persian vocabulary: {}".format(len(persian_islamicate_vocabulary)))
    print("intersection: {} ".format(len(islamicate_intersection)))
    print('\n')
    with open('{}islamicate_intersection.txt'.format(directory), 'w') as out_file:
        for w in islamicate_intersection:
            out_file.write(w+'\n')

    with open('{}islamicate_intersection_sample.txt'.format(directory), 'w') as out_file:
        sample = random.sample(list(islamicate_intersection), round((len(islamicate_intersection) / 100)) * 2)
        for w in sample:
            out_file.write(w+'\n')

    # Print Baha'i stats
    print("Bahá'í language statistics:")
    print("Arabic word count: {}".format(arabic_bahai_word_count))
    print("Persian word count: {}".format(persian_bahai_word_count))
    print("Arabic vocabulary: {}".format(len(arabic_bahai_vocabulary)))
    print("Persian vocabulary: {}".format(len(persian_bahai_vocabulary)))
    print("intersection: {} ".format(len(bahai_intersection)))
    print('\n')

    with open('{}bahai_intersection.txt'.format(directory), 'w') as out_file:
        for w in bahai_intersection:
            out_file.write(w+'\n')

    with open('{}bahai_intersection_sample.txt'.format(directory), 'w') as out_file:
        sample = random.sample(list(bahai_intersection), round((len(bahai_intersection) / 100)) * 2)
        for w in sample:
            out_file.write(w+'\n')

    # Plot table
    data = [[4242, 15, 1927, 2],
            [30000, 2000, 20000, 22000]]

    columns = ("`Abdu'l-Bahá", "Báb", "Bahá'u'lláh", "Shoghi Effendi")
    rows = ["Sample", "Known works"]

    # values = np.arange(0, 2500, 500)
    # value_increment = 1000

    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4

    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
    plot = plt.table(cellText=None, cellColours=None, cellLoc='right', colWidths=None, rowLabels=rows, rowColours=None, rowLoc='left', colLabels=columns, colColours=None, colLoc='center', loc='bottom', bbox=None, edges='closed', **kwargs)
    plot.show()

if __name__ == "__main__":
    main()
