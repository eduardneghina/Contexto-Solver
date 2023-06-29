import time
import re
import random
import gensim.downloader as api
from WebController import *
class AI:
    def __init__(self):
        self._model = api.load('glove-wiki-gigaword-50')
    def __all_words_from_contexto_txt(self): # demo printing them DEMO #3 // cele mai utilizate cuvinte din contexto, in general reciclate, poate le folosim
        with open('extracted_data_example.txt', 'r') as file:
            file_contents_raw = file.read()
        file_content = re.sub('[^a-zA-Z]+', ' ', file_contents_raw).split()
        all_words_from_contexto = list(set(file_content))
        return all_words_from_contexto

    def get_similar_words(self, word):
        similar_words = self._model.most_similar(word, restrict_vocab=10000) # doar 10.000 de links/tokens something ca sa fie rapid/decent
        return similar_words

    def try_random_noun_until_find(self, driver):
        web = WebController(driver)
        web.click_desired_previous_games(100) # hardcoded game 100 for no reason for testing #demo 4
        random_words = self.__all_words_from_contexto_txt()
        while True:
            try:
                type = random.sample(random_words, 1)[0] # scoatem cuvintele deja incercate
                random_words.remove(type)
                web.insert_a_word(type)
            except:
                print("done?! checkit")
