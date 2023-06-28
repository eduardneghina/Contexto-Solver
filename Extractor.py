import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import json
import time
from WebController import *

class Extractor:
    def __init__(self, driver):
        self._driver = driver

    def save(self, path):
        json.dump(self.data, open(path, 'w'))

    def load(self, path):
        self.data = json.load(open(path))

    def extract_game_data(self, game_number, driver):
        webcontrol = WebController(self._driver)
        webcontrol.click_desired_previous_games(game_number)
        webcontrol.click_give_up()
        time.sleep(3)
        webcontrol.click_closest_word()
        time.sleep(3)
        data = []
        elements = self._driver.find_elements(By.CLASS_NAME, 'row-wrapper')
        for e in elements:
            data.append(e.text.split('\n'))
        # filtru duplicate
        res = []
        [res.append(x) for x in data if x not in res]
        return res

    def extract_all_history_games(self): # WARNING ! Incepe de la jocul 1 pana la ultimul si scoate toate datele . DEMO #1 - PLEASE CHECK DEMOS FOLDERS
        webcontrol = WebController(self._driver)
        time.sleep(1)
        a = self._driver.find_element(By.CLASS_NAME, 'info-bar')
        gamenr = a.text[7:10]
        for i in range(int(gamenr)):
            data = self.extract_game_data(i+1, self._driver)
            print(data)
            time.sleep(1)
            b = self._driver.find_element(By.CLASS_NAME, "modal-close-button")
            b.click()
            time.sleep(1)

