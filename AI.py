import time
import re
import gensim.downloader as api
class AI:
    def _init_(self):
        self._model = api.load('glove-wiki-gigaword-50')
        