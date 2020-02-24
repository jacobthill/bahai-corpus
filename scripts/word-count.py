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
    text = text.replace(u'\u200c',' ') # half space
    text = text.replace(u'\u200d',' ') # zero width joiner
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
dispatcher = {'process_three': [process_three, 'three']}

# Main loop
def main():
    # Iterate through the functions in dispatcher and process the text with each
    for value in dispatcher.values():
        # Declare counter variables
        arabic_count = 0
        persian_count = 0

        for name in file_names:
            if 'ar.txt' in name:
                with open(name, 'r') as f:
                    #### Error, use Counter instead of set? ####
                    words = value[0](f.read()).split(' ')
                    arabic_count += len(words)
            else:
                with open(name, 'r') as f:
                    #### Error, use Counter instead of set? ####
                    words = value[0](f.read()).split(' ')
                    persian_count += len(words)

        print('Arabic count: {}\nPersian count: {}'.format(arabic_count, persian_count))

if __name__ == "__main__":
    main()
