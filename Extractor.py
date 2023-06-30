import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import json
import time
from WebController import *

#Clasa extractor scoate in general informatii, le formateaza asa cum le dorim si le trimite mai departe
#Am creat aici si o clasa mostenita pentru exemplu

class Extractor:
    def __init__(self, driver):
        self._driver = driver
        self.data = None

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

    def extract_all_history_games(self): # WARNING ! Incepe de la jocul 1 pana la ultimul si scoate toate datele . DEMO #1 - PLEASE CHECK DEMOS FOLDERS # ~4 games/min save rate
        webcontrol = WebController(self._driver)
        time.sleep(1)
        a = self._driver.find_element(By.CLASS_NAME, 'info-bar')
        gamenr = a.text[7:10]
        for i in range(int(gamenr)):
            time.sleep(1)
            try:
                data = self.extract_game_data(i+1, self._driver)
                print(data)
            except:
                print("e gol lol")
                pass
            else:
                b = self._driver.find_element(By.CLASS_NAME, "modal-close-button")
                b.click()
                time.sleep(1)
                text = TextData()
                datafile = text.load_data()
                if datafile is None:
                    text.save_data(str(data))
                else:
                    text.add_data(str(data))


class TextData(Extractor):
    def __init__(self):  # Hardcoded - path variable should be as a param.
        self.path = "C:\\Contexto\\data.txt"

    def load_data(self):
        try:
            with open(self.path, "r") as infile:
                data = infile.read()
            return data
        except FileNotFoundError:
            print("File not found.")
            return None

    def save_data(self, data):
        with open(self.path, "w") as outfile:
            outfile.write(data)

    def add_data(self, new_data):
        data = self.load_data()
        data += "\n" + new_data
        self.save_data(data)