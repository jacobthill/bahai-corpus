import glob, os
from collections import Counter
from helper import process, build_corpus

# Gather all file names
root_dir = '/Users/jtim/Dropbox/Academic/Sources/Corpora/bahai-works/data/'
authors = ['bahaullah']
languages = ['ar', 'fa']

file_names = build_corpus(root_dir, authors, languages)

directory = '/Users/jtim/Dropbox/Academic/Research/dissertation/research/output/pure-persian/'
if not os.path.exists(directory):
    os.makedirs(directory)

def main():
    pure_persian_works = []
    arabic_counter = Counter()
    arabic_vocabulary = set()

    for name in file_names:
        if 'ar.txt' in name:
            with open("{}{}".format(root_dir, name), 'r') as f:
                #### Error, use Counter instead of set? ####
                words = set(process(f.read()).split())
                arabic_counter.update(words)
                arabic_vocabulary.update(words)

    # remove infrequent words
    for word, count in arabic_counter.items():
        if len(word) < 3: # drop one and two letter words; they have high probablity of being a homograph
            arabic_vocabulary.remove(word)
        elif count <= 2:
            arabic_vocabulary.remove(word)

    with open("{}pure-persian.txt".format(directory), 'w') as out_file:
        for name in file_names:
            if 'fa.txt' in name:
                with open("{}{}".format(root_dir, name), 'r') as f:
                    #### Error, use Counter instead of set? ####
                    words = set(process(f.read()).split())
                    if len(words - arabic_vocabulary) > len(words) * .70: # if x percent of words not in Arabic vocabulary
                        out_file.write(name+"\n")
                        out_file.write("Number of words: {}\n".format(len(words)))
                        out_file.write("Percent Persian words: {}\n".format(len(words - arabic_vocabulary) / len(words)))
                        out_file.write("Words of possible Arabic origin: {}\n".format(words.intersection(arabic_vocabulary)))
                        out_file.write("------------------------------\n\n")
                        pure_persian_works.append(name)

        out_file.write("Pure Persian Works:\n")
        for i in pure_persian_works:
            out_file.write("\t"+"-"+i+"\n")

if __name__ == "__main__":
    main()
