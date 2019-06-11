import glob, operator, os, re
from collections import Counter

os.chdir('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/combined-corpus/')
file_names = glob.glob('*.txt')

def normalize_carachters(text):
    # text=re.sub(r'\W+',' ',text)
    # text=re.sub(r' ','',text)
    # text=re.sub(r'\,','',text)
    return text

counter = Counter()
total_number_of_words = 0

for name in file_names:
    with open(name, 'r') as f:
        words = set(normalize_carachters(f.read()).split(' '))
        total_number_of_words += len(words)
        counter.update(words)

# for value in counter.values():
#     word_count += value
# print("Word count: {}\n".format(word_count))

with open('../../output/normalize-characters-1-1.txt', 'w') as out_file:
    out_file.write('Processing: Split on white space, no character normalization.\n\n')
    out_file.write('Number of words in vocabulary: {}\n\n'.format(len(counter)))
    out_file.write('Total number of words: {}\n\n'.format(total_number_of_words))
    for word, count in counter.most_common(1000):
        chars = [ord(_c) for _c in word]
        spaces = ' ' * (12 - len(chars))
        out_file.write("{}\n".format(word))
        out_file.write("Word count: {}{}u{}\n\n".format(count, spaces, chars))
