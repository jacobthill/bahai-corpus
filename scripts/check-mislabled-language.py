import glob, os
from collections import Counter

# Gather all file names
os.chdir('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/bahaullah/text')
file_names = glob.glob('*.txt')

# Final processing steps
def process(text):
    # replace all diacritics
    char = 1611
    for i in range(20):
        text = text.replace(chr(char), "") # decimal
        char += 1
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
    # replace all diacritics, remove garbage values, and normalize charcters
    text = text.replace(chr(1600), "") # tatweel
    text = text.replace(chr(1705), chr(1603)) # kaf
    text = text.replace(chr(1609), chr(1610)) # ya
    text = text.replace(chr(1740), chr(1610)) # ya
    text = text.replace(chr(1574), chr(1610)) # ya
    text = text.strip("")
    return text

# Checks Arabic works to see if they contain Persian text
def main():
    persian_words = ['خواهد', 'بايد', 'نزد', 'نماييد', 'اين', 'نموده', 'شما', 'اوست', 'بگو', 'شود', 'خود', 'هست', 'گشت', 'شويد', 'راه', 'بآن', 'امروز', 'نمايد', 'چون', 'شوند', 'دوستان', 'شده', 'بوده', 'آنكه', 'بود', 'آفتاب', 'اند', 'داده', 'فردا', 'شايد', 'چه', 'نيست', 'را', 'آنچه', 'مانده', 'بيني', 'جان', 'باز', 'اگر', 'است', 'آمد', 'كنيد', 'سرا', 'نما',  'ميشود', 'نمود', 'دار', 'نبوده', 'شوي', 'ميفرمايد', 'دوست']
    corrupt = []
    pure_persian_works = []
    arabic_counter = Counter()
    arabic_vocabulary = set()
    arabic_works_count = 0
    for name in file_names:
        if 'ar.txt' in name:
            corrupt_word_count = 0
            arabic_works_count +=1
            with open(name, 'r') as f:
                words = set(process(f.read()).split())
                arabic_counter.update(words)
                arabic_vocabulary.update(words)
                for word in words:
                    if word in persian_words:
                        corrupt_word_count += 1
                if corrupt_word_count > 10:
                    corrupt.append(name)
    print(corrupt)
    print("{} of {} are corrupted".format(len(corrupt), arabic_works_count))

    # print(pure_persian_works)
if __name__ == "__main__":
    main()
