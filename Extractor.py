import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import json
import time
from WebController import *
class Extractor:
    data = None

    def __init__(self, path):
        if os.path.exists(path):
            self.load(path)
        else:
            self.data = {}

    def save(self, path):
        json.dump(self.data, open(path, 'w'))

    def load(self, path):
        self.data = json.load(open(path))

    def extract_game_data(self, game_number):
        webcontrol = WebController()
        webcontrol.click_desired_previous_games(game_number)
        webcontrol.click_give_up()
        webcontrol.click_closest_word()
        #collect data , put it somewhere, do some while / for -> outpur json/txt

