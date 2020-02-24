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
    for author in by_author:
        tokens = by_author[author].split()

        # Filter out punctuation
        by_author_tokens[author] = ([process(token) for token in tokens
                                                if any(c.isalpha() for c in token)])



        # Get a distribution of token lengths
        token_lengths = [len(token) for token in by_author_tokens[author]]
        plt.ion()
        by_author_length_distributions[author] = nltk.FreqDist(token_lengths)
        by_author_length_distributions[author].plot(15,title=author,color='grey')
        plt.savefig('{}figures/word-length-{}.png'.format(directory, author))
        plt.ioff()
        plt.close("all")

    ### Chi-squared tests ###

    # Test 1: Compare the distance of Bahá'u'lláh's full corpus to His Baghdad writings
    # and the distance of Shaykh Murtaḍá's writings to Bahá'u'lláh's Baghdad writings
    authors_one = ("Bahá'u'llah", "al-Shaykh Murtaḍá al-Ánsárí")

    for author in authors_one:

        # First, build a joint corpus and identify the 500 most frequent words in it
        joint_corpus = (by_author_tokens[author] + by_author_tokens["Bahá'u'llah Baghdad"])
        joint_freq_dist = nltk.FreqDist(joint_corpus)
        most_common = list(joint_freq_dist.most_common(500))

        # What proportion of the joint corpus is made up of the candidate
        # author's (Bahá'u'llah and Shaykh Murtaḍá) tokens?
        author_share = (len(by_author_tokens[author])
                        / len(joint_corpus))

        # Now, let's look at the 500 most common words in the candidate
        # author's (Bahá'u'llah and Shaykh Murtaḍá) corpus and compare
        # the number of times they can be observed to what would be expected
        # if the author's writings and Bahá'u'llah's Baghdad writings were
        # both random samples from the same distribution.
        chisquared = 0
        for word, joint_count in most_common:

            # How often do we really see this common word?
            author_count = by_author_tokens[author].count(word)
            baghdad_count = by_author_tokens["Bahá'u'llah Baghdad"].count(word)

            # How often should we see it?
            expected_author_count = joint_count * author_share
            expected_joint_count = joint_count * (1-author_share)

            # Add the word's contribution to the chi-squared statistic
            chisquared += ((author_count-expected_author_count) *
                           (author_count-expected_author_count) /
                           expected_author_count)

            chisquared += ((baghdad_count-expected_joint_count) *
                           (baghdad_count-expected_joint_count)
                           / expected_joint_count)

        print("The Chi-squared statistic for", author, "compared to Bahá'u'llah's Baghdad writngs is", chisquared)

        # Test 2: Now consider the relative distance between the writings or `Abdu'l-Bahá`
        # and the writings of Bahá'u'lláh compared to the writings of Shaykh Murtaḍá.
        authors_two = ("`Abdu'l-Bahá", "al-Shaykh Murtaḍá al-Ánsárí")

        for author in authors_two:

            # First, build a joint corpus and identify the 500 most frequent words in it
            joint_corpus = (by_author_tokens[author] + by_author_tokens["Bahá'u'llah"])
            joint_freq_dist = nltk.FreqDist(joint_corpus)
            most_common = list(joint_freq_dist.most_common(500))

            # What proportion of the joint corpus is made up of the candidate
            # author's (`Abdu'l-Bahá` and Shaykh Murtaḍá) tokens?
            author_share = (len(by_author_tokens[author])
                            / len(joint_corpus))

            # Now, let's look at the 500 most common words in the candidate
            # author's (`Abdu'l-Bahá` and Shaykh Murtaḍá) corpus and compare
            # the number of times they can be observed to what would be expected
            # if the author's writings and Bahá'u'llah's writings were both
            # random samples from the same distribution.
            chisquared = 0
            for word, joint_count in most_common:

                # How often do we really see this common word?
                author_count = by_author_tokens[author].count(word)
                baghdad_count = by_author_tokens["Bahá'u'llah"].count(word)

                # How often should we see it?
                expected_author_count = joint_count * author_share
                expected_joint_count = joint_count * (1-author_share)

                # Add the word's contribution to the chi-squared statistic
                chisquared += ((author_count-expected_author_count) *
                               (author_count-expected_author_count) /
                               expected_author_count)

                chisquared += ((baghdad_count-expected_joint_count) *
                               (baghdad_count-expected_joint_count)
                               / expected_joint_count)

            print("The Chi-squared statistic for", author, "compared to Bahá'u'llah's writngs is", chisquared)

if __name__ == "__main__":
    main()
