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
# WebController este o clasa in care gasim metodele care ne lasa sa interctionam
# cu Contexto la nivel de browser.
# Am creat mai multe metode utile pentru interactiunea cu contexto.me
#
#
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

    # private, needed only for the next method
    def __click_yes_for_give_up(self):
        elements = self._driver.find_elements(By.CLASS_NAME, 'share-btn')
        for e in elements:
            if e.text == 'Yes':
                e.click()
                break

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

