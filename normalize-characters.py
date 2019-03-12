import nltk

in_file = "/Users/jtim/Dropbox/Academic/sources/bahai-corpus/data/bahaullah/text/bahaullah-kb-fa.txt"

with open (in_file, 'r') as f:
    f = f.read()
    words = f.split()

    fdist = nltk.FreqDist(words)
    out_file = open('vocabulary.txt', 'w')

    # for w in words:
    #     out_file.write(w.encode(encoding='UTF-16',errors='strict'))
    #
    for word, frequency in fdist.most_common(1000):
        for _c in word: #print('U+%04x' % ord(_c))
        # binary = word.encode(encoding='UTF-16',errors='strict')
            out_file.write('U+{} '.format(ord(_c)))
        out_file.write(': F={}: {}\n'.format(word, frequency))


# with open(in_file, "rb") as f:
#     byte = f.read(1)
#     while byte != b"":
#         byte = f.read()
