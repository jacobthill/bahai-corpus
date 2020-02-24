from helper import build_corpus, process
import glob, nltk, os
import matplotlib.pyplot as plt

# Gather corpora
base_dir = '/Users/jtim/Dropbox/Academic/sources/corpora/'
bahaullah = build_corpus('{}bahai-works/data/'.format(base_dir), ['bahaullah'], ['ar'])
abdulbaha = build_corpus('{}bahai-works/data/'.format(base_dir), ['abdulbaha'], ['ar'])
bab = build_corpus('{}bahai-works/data/'.format(base_dir), ['bab'], ['ar'])
murtada_ansari = glob.glob('/Users/jtim/Dropbox/Academic/sources/corpora/open-arabic-1300AH/data/1281MurtadaAnsari/*/arc/*.txt')
bahaullah_baghdad = ['bahaullah-anbka-15-ar.txt', # سورة الذكر
                     'bahaullah-aqa2-67-ar.txt', # جواهر الاسرار
                     'bahaullah-aqa2-93-ar.txt', # سورة القدير
                     'bahaullah-aqa2-76-ar.txt', # سورة الله
                     'bahaullah-aqa2-101-ar.txt', # لوح الحورية
                     'bahaullah-km-1-ar.txt', # الكلمات المكنونة العربية
                     'bahaullah-st-010-1-ar.txt', # الحروفات العاليات
                     'bahaullah-st-029-ar.txt', # (لوح آية النور (تفسير الحروفات المقطعة
                     'bahaullah-st-037-ar.txt', # لوح الفتنة
                     'bahaullah-st-041-ar.txt', # لوح الحق
                     'bahaullah-st-052-ar.txt', # لوح كل الطعام
                     'bahaullah-st-087-ar.txt', # لوح مدينة الرضا
                     'bahaullah-st-088-ar.txt', # لوح مدينة التوحيد
                     'bahaullah-st-100-ar.txt', # لوح سبحان ربي الاعلى
                     'bahaullah-st-133-ar.txt', # سورة النصح
                     'bahaullah-st-138-ar.txt', # (سورة الصبر (لوح ايوب
                     'bahaullah-st-144-ar.txt' # تفسير هو
                     ]

# Update items in bahaullah_baghdad to full file path
for idx, item in enumerate(bahaullah_baghdad):
   item = "{}bahai-works/data/bahaullah/text/{}".format(base_dir, item)
   bahaullah_baghdad[idx] = item

# Map corpora names to corpora
corpora = {"Bahá'u'llah": bahaullah,
           "Bahá'u'llah's Arabic Baghdad Writings": bahaullah_baghdad,
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

# Compare a list of candidate authors to a relative corpus using the chi-squared method
def chi_squared(relative_corpus, authors = []):
    by_author = {}
    for key, files in corpora.items():
        by_author[key] = read_files_into_string(files)

    # Transform the authors' corpora into lists of word tokens
    by_author_tokens = {}
    by_author_length_distributions = {}
    for author in by_author:
        tokens = by_author[author].split()

        # Filter out punctuation
        by_author_tokens[author] = ([process(token) for token in tokens
                                                if any(c.isalpha() for c in token)])

    for author in authors:

        # First, build a joint corpus and identify the 500 most frequent words in it
        joint_corpus = (by_author_tokens[author] + by_author_tokens[relative_corpus])
        joint_freq_dist = nltk.FreqDist(joint_corpus)
        most_common = list(joint_freq_dist.most_common(500))

        # What proportion of the joint corpus is made up of the candidate
        # author's tokens?
        author_share = (len(by_author_tokens[author])
                        / len(joint_corpus))

        # Now, let's look at the 500 most common words in the candidate
        # author's corpus and compare the number of times they can be observed
        # to what would be expected if the author's writings and the relative
        # corpus were both random samples from the same distribution.
        chisquared = 0
        for word, joint_count in most_common:

            # How often do we really see this common word?
            author_count = by_author_tokens[author].count(word)
            relative_count = by_author_tokens[relative_corpus].count(word)

            # How often should we see it?
            expected_author_count = joint_count * author_share
            expected_joint_count = joint_count * (1-author_share)

            # Add the word's contribution to the chi-squared statistic
            chisquared += ((author_count-expected_author_count) *
                           (author_count-expected_author_count) /
                           expected_author_count)

            chisquared += ((relative_count-expected_joint_count) *
                           (relative_count-expected_joint_count)
                           / expected_joint_count)

        print("The Chi-squared statistic for", author, "compared to", relative_corpus, "is", chisquared)

def main():
    directory = '/Users/jtim/Dropbox/Academic/research/dissertation/research/output/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    ### Chi-squared tests ###

    # Test 1: Compare the distance of Bahá'u'lláh's full corpus to His Baghdad writings
    # and the distance of Shaykh Murtaḍá's writings to Bahá'u'lláh's Baghdad writings.
    authors_one = ["Bahá'u'llah", "al-Shaykh Murtaḍá al-Ánsárí"]
    chi_squared("Bahá'u'llah's Arabic Baghdad Writings", authors_one)

    # Test 2: Now consider the relative distance between the writings of `Abdu'l-Bahá`,
    # the Báb, and Shaykh Murtaḍá compared to those of Bahá'u'lláh.
    authors_two = ["`Abdu'l-Bahá", "al-Shaykh Murtaḍá al-Ánsárí", "the Báb"]
    chi_squared("Bahá'u'llah", authors_two)

    # Test 3: Now consider the relative distance between the writings of `Abdu'l-Bahá`,
    # and Shaykh Murtaḍá compared to those of the Báb.
    authors_three = ["`Abdu'l-Bahá", "al-Shaykh Murtaḍá al-Ánsárí"]
    chi_squared("the Báb", authors_three)

    # Test 4: Finally, consider the relative distance between the writings of `Abdu'l-Bahá`,
    # and those of Shaykh Murtaḍá.
    authors_four = ["`Abdu'l-Bahá"]
    chi_squared("al-Shaykh Murtaḍá al-Ánsárí", authors_four)

if __name__ == "__main__":
    main()
