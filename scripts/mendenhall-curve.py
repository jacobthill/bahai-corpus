from helper import build_corpus, process
import glob, nltk, os
import matplotlib.pyplot as plt

# Gather corpora
base_dir = '/Users/jtim/Dropbox/Academic/sources/corpora/'
bahaullah = build_corpus('{}bahai-works/data/'.format(base_dir), ['bahaullah'], ['ar'])
abdulbaha = build_corpus('{}bahai-works/data/'.format(base_dir), ['abdulbaha'], ['ar'])
bab = build_corpus('{}bahai-works/data/'.format(base_dir), ['bab'], ['ar'])
murtada_ansari = glob.glob('/Users/jtim/Dropbox/Academic/sources/corpora/open-arabic-1300AH/data/1281MurtadaAnsari/*/arc/*.txt')
bahaullah_baghdad = ['bahaullah-st-052-ar.txt', 'bahaullah-km-1-ar.txt', 'bahaullah-aqa2-67-ar.txt', 'bahaullah-st-138-ar.txt',
                     'bahaullah-st-87-ar.txt', 'bahaullah-st-088-ar.txt', 'bahaullah-aqa2-93-ar.txt', 'bahaullah-st-029-ar.txt',
                     'bahaullah-st-010-1-ar.txt', 'bahaullah-st-133-ar.txt', 'bahaullah-aqa2-101-ar.txt']

# Update items in bahaullah_baghdad to full file path
for idx, item in enumerate(bahaullah_baghdad):
   item = "{}bahai-works/data/bahaullah/text/{}".format(base_dir, item)
   bahaullah_baghdad[idx] = item

# Map corpora names to corpora
corpora = {"Bahá'u'llah": bahaullah,
           "Bahá'u'llah Baghdad": bahaullah_baghdad,
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
    directory = '/Users/jtim/Dropbox/Academic/research/dissertation/research/output/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    by_author = {}
    for author, files in corpora.items():
        by_author[author] = read_files_into_string(files)

    authors = ("Bahá'u'llah", "Bahá'u'llah Baghdad", "`Abdu'l-Bahá", "the Báb", "al-Shaykh Murtaḍá al-Ánsárí")

    # Transform the authors' corpora into lists of word tokens
    by_author_tokens = {}
    by_author_length_distributions = {}
    for author in authors:
        tokens = by_author[author].split()

        # Filter out punctuation
        by_author_tokens[author] = ([token for token in tokens
                                                if any(c.isalpha() for c in token)])

        # Get a distribution of token lengths
        token_lengths = [len(token) for token in by_author_tokens[author]]
        plt.ion()
        by_author_length_distributions[author] = nltk.FreqDist(token_lengths)
        by_author_length_distributions[author].plot(15,title=author,color='grey')
        plt.savefig('{}figures/word-length-{}.png'.format(directory, author))
        plt.ioff()
        plt.close("all")

    ### Chi-squared test ###

    # First, build a joint corpus and identify the 500 most frequent words in it
    full_corpus = by_author_tokens["Bahá'u'llah"]
    baghdad = by_author_tokens["Bahá'u'llah Baghdad"]
    joint_freq_dist = nltk.FreqDist(full_corpus)
    most_common = list(joint_freq_dist.most_common(500))

    # What proportion of the joint corpus is made up
    # of the candidate author's tokens?
    author_share = (len(by_author_tokens["Bahá'u'llah Baghdad"])
                    / len(full_corpus))

    # Now, let's look at the 500 most common words in the candidate
    # author's corpus and compare the number of times they can be observed
    # to what would be expected if the author's papers
    # and the Disputed papers were both random samples from the same distribution.
    chisquared = 0
    for word,full_corpus_count in most_common:

        # How often do we really see this common word?
        author_count = by_author_tokens["Bahá'u'llah"].count(word)
        baghdad_count = by_author_tokens["Bahá'u'llah Baghdad"].count(word)

        # How often should we see it?
        expected_author_count = full_corpus_count * author_share
        expected_baghdad_count = full_corpus_count * (1-author_share)

        # Add the word's contribution to the chi-squared statistic
        chisquared += ((author_count-expected_author_count) *
                       (author_count-expected_author_count) /
                       expected_author_count)

        chisquared += ((baghdad_count-expected_baghdad_count) *
                       (baghdad_count-expected_baghdad_count)
                       / expected_baghdad_count)

    # print("{} - {} * {} {} / {}".format(author_count, expected_author_count, author_count, expected_author_count, expected_author_count))

    print("The Chi-squared statistic for", author, "is", chisquared)

if __name__ == "__main__":
    main()
