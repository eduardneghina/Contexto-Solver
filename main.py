import time
from WebController import *
from Database import *
from Extractor import *
from AI import *

driver = initiate_contexto()
controller = WebController(driver)


controller.insert_a_word("house")
time.sleep(1)
controller.insert_a_word("dog")
time.sleep(1)
controller.insert_a_word("cat")
time.sleep(1)
controller.insert_a_word("meat")
time.sleep(1)
controller.insert_a_word("wood")
time.sleep(1)
a = controller.get_words_and_ids_list()

print(a)
# output INSFARSIT LISTA CORECTA : [('wood', '152'), ('house', '392'), ('dog', '1809'), ('cat', '2985'), ('meat', '3335')]