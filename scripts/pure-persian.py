import glob, os
from collections import Counter
from helper import process

# Gather all file names
os.chdir('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/bahaullah/text')
file_names = glob.glob('*.txt')

def main():
    pure_persian_works = []
    arabic_counter = Counter()
    arabic_vocabulary = set()

    for name in file_names:
        if 'ar.txt' in name:
            with open(name, 'r') as f:
                words = set(process(f.read()).split())
                arabic_counter.update(words)
                arabic_vocabulary.update(words)

    # remove infrequent words
    for word, count in arabic_counter.items():
        if len(word) < 3: # drop one and two letter words; they have high probablity of being a homograph
            arabic_vocabulary.remove(word)
        elif count <= 2:
            arabic_vocabulary.remove(word)

    for name in file_names:
        if 'fa.txt' in name:
            with open(name, 'r') as f:
                words = set(process(f.read()).split())
                if len(words - arabic_vocabulary) > len(words) * .70: # if x percent of words not in Arabic vocabulary
                    print(name)
                    print("Number of words: {}".format(len(words)))
                    print("Percent Persian words: {}".format(len(words - arabic_vocabulary) / len(words)))
                    # print("Words of possible Arabic origin: {}".format(words.intersection(arabic_vocabulary)))
                    print("-----------------------")
                    pure_persian_works.append(name)

if __name__ == "__main__":
    main()
