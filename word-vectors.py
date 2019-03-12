import fnmatch, gensim, glob, os
from stanfordnlp.server import CoreNLPClient

def to_str(bytes_or_str):
    '''Takes bytes or string and returns string'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

class MySentences(object):
    def __init__(self, dirname, pattern):
        self.dirname = dirname
        self.pattern = pattern

    def __iter__(self):
        for root, dirnames, filenames in os.walk(self.dirname):
            for filename in fnmatch.filter(filenames, self.pattern):
                for line in open(os.path.join(root, filename)):
                    yield line.split()

arabic_sentences = MySentences('/Users/jtim/Dropbox/Academic/Research/dissertation/research/data/TED/processed', '*ar.txt')

# persian_sentences = MySentences('/Users/jtim/Dropbox/Academic/sources/bahai-corpus/data', '*fa.txt')

ar_model = gensim.models.Word2Vec(arabic_sentences)

# fa_model = gensim.models.Word2Vec(persian_sentences)
#
print(ar_model.wv.most_similar(positive=['الله', 'كتاب'], negative=['ارض'], topn=1))
