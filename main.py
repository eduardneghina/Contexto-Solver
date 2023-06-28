import time
from WebController import *
from Database import *
from Extractor import *

driver = initiate_contexto()
extract = Extractor()
a = extract.extract_game_data(40, driver)
print(a)
# output will be the list from game 40 : ['potato', '1'], ['mash', '2'], ['carrot', '3'], ['onion', '4'], ['vegetable', '5'], ..etc
time.sleep(10)