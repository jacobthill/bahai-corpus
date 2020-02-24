import glob, os
from collections import Counter
from helper import process

# Gather all file names
os.chdir('/Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/bahaullah/text')
file_names = glob.glob('*.txt')

# Checks Arabic works to see if they contain Persian text
def main():
    persian_words = ['خواهد', 'بايد', 'نزد', 'نماييد', 'اين', 'نموده', 'شما', 'اوست', 'بگو', 'شود', 'خود', 'هست', 'گشت', 'شويد', 'راه', 'بآن', 'امروز', 'نمايد', 'چون', 'شوند', 'دوستان', 'شده', 'بوده', 'آنكه', 'بود', 'آفتاب', 'اند', 'داده', 'فردا', 'شايد', 'چه', 'نيست', 'را' , 'آنچه’, 'شود’, ’آنچه', 'مانده', 'بيني', 'جان', 'باز', 'اگر', 'است', 'آمد', 'كنيد', 'سرا', 'نما',  'ميشود', 'نمود', 'دار', 'نبوده', 'شوي', 'ميفرمايد', 'دوست']
    corrupt = []
    pure_persian_works = []
    arabic_counter = Counter()
    arabic_vocabulary = set()
    arabic_works_count = 0
    for name in file_names:
        if 'ar.txt' in name:
            corrupt_word_count = 0
            arabic_works_count += 1
            with open(name, 'r') as f:
                words = set(process(f.read()).split())
                arabic_counter.update(words)
                arabic_vocabulary.update(words)
                for word in words:
                    if word in persian_words:
                        corrupt_word_count += 1
                if corrupt_word_count > 0:
                    corrupt.append(name)
    print(corrupt)
    print("{} of {} are corrupted".format(len(corrupt), arabic_works_count))

    # print(pure_persian_works)
if __name__ == "__main__":
    main()
