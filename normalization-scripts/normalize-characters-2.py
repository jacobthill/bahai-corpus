import glob, operator, os, re
from collections import Counter

os.chdir('/Users/jtim/Dropbox/Academic/sources/bahai-corpus/data/combined-corpus/')
file_names = glob.glob('*.txt')

def remove_garbage(text):
    # text=re.sub(r'.',' ',text)
    text = text.replace(u'\u200c', ' ') # zero width non joiner
    text = text.replace(u'\u202c', ' ') # pop directional formatting
    text = text.replace(u'\u202b', ' | ') # right-to-left embedding
    text = text.replace('.', ' .') # move periods at end of sentence
    text=re.split('[\n\t\r\s\v\f]', text)
    return text

counter = Counter()

total = 0
files = 0
word_count = 0
for name in file_names:
    files += 1
    with open(name, 'r') as f:
        words = set(remove_garbage(f.read()))
        total += len(words)
        counter.update(words)

for value in counter.values():
    word_count += value
print("Word count: {}\n".format(word_count))

with open('../../output/out-1.txt', 'w') as out_file:
    # out_file.write('Processing: Split on white space, no character normalization.\n\n')
    # out_file.write('Number of words in vocabulary: {}\n\n'.format(len(counter)))
    # out_file.write('Total Words: {}\n\n'.format(total))
    # out_file.write('Total Works: {}\n\n'.format(files))
    out_file.write(str(counter.items())) # remove and uncomment above after debugging 
    for word, count in counter.most_common(1000):
        chars = [ord(_c) for _c in word]
        spaces = ' ' * (12 - len(chars))
        out_file.write("{}\n".format(word))
        out_file.write("Word count: {}{}u{}\n\n".format(count, spaces, chars))
