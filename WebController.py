import os
import re
import time
import json
from random_words import RandomWords
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ##############################################################################
# WebController este o clasa in care gasim metodele care ne lasa sa interctionam cu Contexto la nivel de browser.
# Functia de initializare a fost lasata aici deoarece ea paseaza mai departe "driverul" care este controlul catre obiectele/metodele care o cer.
# Astfel, daca initializarea nu se termina cu succes nici nu merge mai departe
# Numele metodelor sunt in general destul de clare, am incercat sa folosesc si metode privat ca exemplu.
# for in elements e cea mai rapida dar si putin volatila metoda, se poate implementa o metoda de wait to exist dar care pentru moment mi s-a parut prea complicata.
# ###############################################################################

# Am lasat functia asta in afara clasei pentru ca nu stiu cum sa o intregrez mai frumos sa returneze driverul dupa initiate
# si ca sa nu fac haos in main.py am lasat aici totul.
# Initiating browser + click consent button + return driver
def initiate_contexto():
    driver = webdriver.Chrome()
    print("Opening browser")
    driver.get("https://contexto.me/")
    driver.maximize_window()
    time.sleep(3)
    try:
        driver.find_element(By.CLASS_NAME, 'fc-primary-button').click()
    except:
        # N-am nici o idee cum sa fac handle la asta in a real way
        print("Consent cookie button could not be pressed. initiate_contexto() failed")
        return False
    else:
        print("Contexto is fully initiated and ready to use")
        return driver

# Class to control Web related actions
class WebController:
    def __init__(self, driver):
        self._driver = driver

    # private, needed only for the methods that use buttons from the 3 dot menu
    def __click_3dots(self):
        elements = self._driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button')
        for e in elements:
            e.click()
            break

    def __click_yes_for_give_up(self):
        elements = self._driver.find_elements(By.CLASS_NAME, 'share-btn')
        for e in elements:
            if e.text == 'Yes':
                e.click()
                break

    def __get_word_and_id_list_raw(self):
        elements = self._driver.find_elements(By.CLASS_NAME, 'guess-history')
        for i in range(10):
            for e in elements:
                a = []
                a.append(e.text)
                return a

    def get_secret_word(self):
        elements = self._driver.find_elements(By.CLASS_NAME, 'row')
        for e in elements:
            return e.text

    def clear_text_area(self):
        elements = self._driver.find_elements(By.CLASS_NAME, 'word')
        for e in elements:
            e.clear()

    def get_word_and_id(self):
        elements = self._driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[2]')
        for e in elements:
            if e is not None:
                a = e.text.split()
                return a

    def get_words_and_ids_list(self): # doar 80 de minute pentru asta, nu am idee de ce merge o.O  # DEMO #2
        a = str(self.__get_word_and_id_list_raw())
        a = a.strip("[]").strip("'").replace("\\n", "\n")
        words = a.split()
        my_list = []
        for i in range(0, len(words) - 1, 2):
            if words[i].isalpha() and words[i + 1].isdigit():
                my_list.append((words[i], words[i + 1]))
        return my_list

    def click_give_up(self):
        self.__click_3dots()
        elements = self._driver.find_elements(By.CLASS_NAME, 'menu-item')
        for e in elements:
            if e.text == 'Give up':
                e.click()
                self.__click_yes_for_give_up()
                break

    def click_previous_games(self):
        self.__click_3dots()
        elements = self._driver.find_elements(By.CLASS_NAME, 'menu-item')
        for e in elements:
            if e.text == 'Previous games':
                e.click()
                break

    def click_closest_word(self):
        elements = self._driver.find_elements(By.CLASS_NAME, 'button')
        for e in elements:
            if e.text == 'Closest words':
                e.click()
                break

    def click_desired_previous_games(self, game_number):
        self.click_previous_games()
        time.sleep(3)
        elements = self._driver.find_elements(By.CLASS_NAME, 'game-selection-button')
        for e in elements:
            if re.search('#' + str(game_number) + '\n', e.text) is not None:
                self._driver.execute_script("arguments[0].scrollIntoView();", e)
                e.click()
                break

    def click_random_previous_game(self):
        self.click_previous_games()
        time.sleep(3)
        elements = self._driver.find_elements(By.CLASS_NAME, 'button')
        for e in elements:
            if e.text == "Random":
                e.click()
                break

    def insert_random_word(self):
        rw = RandomWords()
        random_word = rw.random_word()
        self._driver.find_element(By.NAME, 'word').send_keys(random_word, Keys.ENTER)

    def insert_a_word(self, word):
        elements = self._driver.find_elements(By.CLASS_NAME, 'word')
        for e in elements:
            e.send_keys(str(word))
            # time.sleep(1) <- use this for slow internet :)
            e.send_keys(Keys.ENTER)
            time.sleep(1)



