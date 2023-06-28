import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import json
import time
from WebController import *

class Extractor:
    def __init__(self):
        pass

    def save(self, path):
        json.dump(self.data, open(path, 'w'))

    def load(self, path):
        self.data = json.load(open(path))

    def extract_game_data(self, game_number, driver):
        webcontrol = WebController(driver)
        webcontrol.click_desired_previous_games(game_number)
        webcontrol.click_give_up()
        time.sleep(3)
        webcontrol.click_closest_word()
        time.sleep(3)
        data = []
        elements = driver.find_elements(By.CLASS_NAME, 'row-wrapper')
        for e in elements:
            data.append(e.text.split('\n'))
        return data
