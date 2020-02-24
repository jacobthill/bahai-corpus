from helper import build_corpus, process
import glob, nltk, os
import matplotlib.pyplot as plt

# Gather corpora
base_dir = '/Users/jtim/Dropbox/Academic/sources/corpora/'
bahaullah = build_corpus('{}bahai-works/data/'.format(base_dir), ['bahaullah'], ['ar'])
abdulbaha = build_corpus('{}bahai-works/data/'.format(base_dir), ['abdulbaha'], ['ar'])
bab = build_corpus('{}bahai-works/data/'.format(base_dir), ['bab'], ['ar'])
murtada_ansari = glob.glob('/Users/jtim/Dropbox/Academic/sources/corpora/open-arabic-1300AH/data/1281MurtadaAnsari/*/arc/*.txt')

# Map corpora names to corpora
corpora = {"Bahá'u'llah": bahaullah,
           "`Abdu'l-Bahá": abdulbaha,
           "the Báb": bab,
           "al-Shaykh Murtaḍá al-Ánsárí": murtada_ansari}

# Read files into string, remove junk, remove diacritics, normalize characters
def read_files_into_string(filenames):
    strings = []
    for filename in filenames:
        with open(filename) as f:
            strings.append(process(f.read()))
    return '\n'.join(strings)

def main():
    directory = '/Users/jtim/Dropbox/Academic/research/dissertation/research/output/word-length'
    if not os.path.exists(directory):
        os.makedirs(directory)
    by_author = {}
    for author, files in corpora.items():
        by_author[author] = read_files_into_string(files)

    # Transform the authors' corpora into lists of word tokens
    by_author_tokens = {}
    by_author_length_distributions = {}
    for author in by_author:
        tokens = by_author[author].split()

        # Filter out punctuation
        by_author_tokens[author] = ([process(token) for token in tokens
                                                if any(c.isalpha() for c in token)])

        # Get a distribution of token lengths
        token_lengths = [len(token) for token in by_author_tokens[author]]
        plt.ion()
        by_author_length_distributions[author] = nltk.FreqDist(token_lengths)
        by_author_length_distributions[author].plot(9,title=author,color='grey')
        plt.savefig('{}/word-length-{}.png'.format(directory, author))
        plt.ioff()
        plt.close("all")



if __name__ == "__main__":
    main()
