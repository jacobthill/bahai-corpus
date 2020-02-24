import glob, os
from collections import Counter
from helper import process, build_corpus

# # Gather all file names
root_dir = '/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/'
authors = ['bahaullah']
languages = ['ar', 'fa']

file_names = build_corpus(root_dir, authors, languages)

directory = '/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/output/language-data/'
if not os.path.exists(directory):
    os.makedirs(directory)

def main():
    pure_arabic_works = []
    pure_persian_works = []
    arabic_counter = Counter()
    arabic_vocabulary = set()
    persian_counter = Counter()
    persian_vocabulary = set()
    a_count = 0
    for name in file_names:
        if 'ar.txt' in name:
            a_count += 1
            with open("{}{}".format(root_dir, name), 'r') as f:
                #### Error, use Counter instead of set? ####
                words = set(process(f.read()).split())
                arabic_counter.update(words)
                arabic_vocabulary.update(words)

    for name in file_names:
        if 'fa.txt' in name:
            with open("{}{}".format(root_dir, name), 'r') as f:
                #### Error, use Counter instead of set? ####
                words = set(process(f.read()).split())
                persian_counter.update(words)
                persian_vocabulary.update(words)

    # remove infrequent words
    count = 2
    for word, count in arabic_counter.items():
        if len(word) < 3: # drop one and two letter words; they have high probablity of being a homograph
            arabic_vocabulary.remove(word)

        elif count < count:
            arabic_vocabulary.remove(word)

    for word, count in persian_counter.items():
        if count < count:
            persian_vocabulary.remove(word)

    with open("{}pure-persian.txt".format(directory), 'w') as out_file:
        for name in file_names:
            if 'fa.txt' in name:
                with open("{}{}".format(root_dir, name), 'r') as f:
                    words = set(process(f.read()).split())
                    if len(words - arabic_vocabulary) > len(words) * .70: # if x percent of words not in Arabic vocabulary
                        out_file.write(name+"\n")
                        out_file.write("Number of words: {}\n".format(len(words)))
                        out_file.write("Percent Persian words: {}\n".format(len(words - arabic_vocabulary) / len(words)))
                        out_file.write("Words of possible Arabic origin: {}\n".format(words.intersection(arabic_vocabulary)))
                        out_file.write("------------------------------\n\n")
                        pure_persian_works.append(name)

        out_file.write("{} Pure Persian works found:\n".format(len(pure_persian_works)))
        for i in pure_persian_works:
            out_file.write("\t"+"-"+i+"\n")

    with open("{}pure-arabic.txt".format(directory), 'w') as out_file:
        for name in file_names:
            if 'ar.txt' in name:
                with open("{}{}".format(root_dir, name), 'r') as f:
                    words = set(process(f.read()).split())
                    if len(words.intersection(persian_vocabulary)) > (len(words) * .99): # if x percent of words not in Persian vocabulary
                        out_file.write(name+"\n")
                        out_file.write("Number of words: {}\n".format(len(words)))
                        out_file.write("Percent Persian words: {}\n".format(len(words - arabic_vocabulary) / len(words)))
                        out_file.write("Words of possible Arabic origin: {}\n".format(words.intersection(arabic_vocabulary)))
                        out_file.write("------------------------------\n\n")
                        pure_arabic_works.append(name)

        out_file.write("{} Pure Arabic works found:\n".format(len(pure_arabic_works)))
        for i in pure_arabic_works:
            out_file.write("\t"+"-"+i+"\n")

    # Figure out how to write a set of Words
    with open("{}boundary-words.txt".format(directory), 'w') as out_file:
        out_file.write(arabic_vocabulary.intersection(persian_vocabulary))

if __name__ == "__main__":
    main()
