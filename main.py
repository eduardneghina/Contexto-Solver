import time
from WebController import *
from Database import *
from Extractor import *

driver = initiate_contexto()
extractor = Extractor(driver)
extractor.extract_all_history_games()