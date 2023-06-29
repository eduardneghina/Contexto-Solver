import time
import re
import gensim.downloader as api
class AI:
    def __init__(self):
        self._model = api.load('glove-wiki-gigaword-50')

    def get_similar_words(self, word):
        similar_words = self._model.most_similar(word, restrict_vocab=10000) # doar 10.000 ca sa fie rapid/decent
        return similar_words
