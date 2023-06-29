import time
from WebController import *
from Database import *
from Extractor import *
from AI import *

driver = initiate_contexto()
controller = WebController(driver)

controller.insert_a_word("lasting")
time.sleep(1)
print(controller.get_word_and_id())
# output ex : ['last', '680'] - first the word and than the id
