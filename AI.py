import time
import re
import random
import gensim.downloader as api
from WebController import *
################################
# Clasa de AI aduna cele mai importante functii si metode si le pune cap la cap pentru a ajunge la rezultatul dorit, in cazul nostru cuvantul secret
# modelul glove-wiki-gigaword-50 este unul dintre cele mai mici dar destul de complex, avantaj ca poate fi descarcat prin api direct de user
################################
class AI:
    def __init__(self):
        self._model = api.load('glove-wiki-gigaword-50')
    def __all_words_from_contexto_txt(self): # demo printing them DEMO #3 // cele mai utilizate cuvinte din contexto, in general reciclate, poate le folosim
        with open('extracted_data_example.txt', 'r') as file:
            file_contents_raw = file.read()
        file_content = re.sub('[^a-zA-Z]+', ' ', file_contents_raw).split()
        all_words_from_contexto = list(set(file_content))
        return all_words_from_contexto

    def __refactor_list_similar_words(self, list):
        list_to_return = re.sub('[^a-zA-Z]+', ' ', str(list)).split()
        return list_to_return

    def give_up_and_return_the_word(self, driver, game_number):
        web = WebController(driver)
        web.click_desired_previous_games(game_number)
        time.sleep(1)
        web.click_give_up()
        time.sleep(1)
        a = web.get_secret_word()
        return a

    def get_similar_words(self, word):
        similar_words = self._model.most_similar(word, restrict_vocab=20000) # increased to 20k 
        return similar_words

    def try_random_noun_until_find(self, driver, game_number):
        web = WebController(driver)
        if game_number is not None:
            web.click_desired_previous_games(game_number)
        else:
            pass
        random_words = self.__all_words_from_contexto_txt()
        while True:
            try:
                to_be_typed = random.sample(random_words, 1)[0] # scoatem cuvintele deja incercate
                random_words.remove(to_be_typed)
                web.insert_a_word(to_be_typed)
            except:
                print("done?! checkit") # to be done more nice in the future
                break

    def try_smart_ish(self, driver, game_number): # DEMO 5
        web = WebController(driver)
        if game_number is not None:
            web.click_desired_previous_games(game_number)
        else:
            pass
        random_words = self.__all_words_from_contexto_txt()
        for i in range(10):
            type = random.sample(random_words, 1)[0]  # scoatem cuvintele deja incercate
            random_words.remove(type)
            web.insert_a_word(type)

        global first_run
        global sml_words
        first_run = True

        while True:  # id - most_close[0][1] // word - most_close[0][0]
            most_close = web.get_words_and_ids_list()
            similar_words_raw = self.get_similar_words(most_close[0][0])
            similar_words = self.__refactor_list_similar_words(similar_words_raw)
            if first_run is True:
                first_run = False
                for e in similar_words:
                    web.insert_a_word(e)
                    web.clear_text_area()
            else:
                if sml_words == similar_words:
                    for e in similar_words:
                        web.insert_a_word(e)
                        web.clear_text_area()
                        random_words = self.__all_words_from_contexto_txt()
                        for i in range(10):
                            type = random.sample(random_words, 1)[0]  # scoatem cuvintele deja incercate
                            random_words.remove(type)
                            web.insert_a_word(type)
                else:
                    for e in similar_words:
                        web.insert_a_word(e)
                        web.clear_text_area()
            sml_words = similar_words

            if most_close[0][1] == "1":
                print("Cuvantul secret era: " + similar_words[0] )
                break
            else:
                pass
        else:
            pass