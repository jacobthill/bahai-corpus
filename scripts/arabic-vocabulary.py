import glob, os
from collections import Counter
from helper import process, build_corpus

dir = "/Users/jtim/Dropbox/Academic/sources/corpora/bahai-works/data/"
authors = ['abdulbaha']
languages = ['ar']

corpus = build_corpus(dir, authors, languages)

mmha1 = []


arabic_counter = Counter()

for name in corpus:
    if 'mmha1' in name:
        mmha1.append(name)

for file in mmha1:
    with open("{}{}".format(dir, name), 'r') as f, open('/Users/jtim/Desktop/out.txt', 'w') as out:
        out.write(file)
        out.write('\n')
        out.write("--------------------------------------")
        out.write('\n')
        out.write(f.read())

for file in mmha1:
    with open("{}{}".format(dir, name), 'r') as f, open('/Users/jtim/Desktop/out.txt', 'w') as out_c:
        words = Counter(process(f.read()).split())
        arabic_counter.update(words)
        out_c.write(f.read())
        out_c.write('\n')
        out_c.write("--------------------------------------")
        out_c.write('\n')
        out_c.write(str(words))


# print(len(mmha1))
# print(len(arabic_counter))
# print(arabic_counter.most_common(10000))
