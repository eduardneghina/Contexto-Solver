import time
from WebController import *
from Database import *
from Extractor import *
from AI import *

#driver = initiate_contexto()

ai = AI()
print(ai.get_similar_words("food"))
# output top 1: products
# last 9 with vectors : ('coffee', 0.7853199243545532), ('supplies', 0.7699311375617981), ('meat', 0.769260823726654),
#  ('foods', 0.7517945766448975), ('supply', 0.7429676651954651), ('goods', 0.7426424026489258), ('items', 0.7383918166160583), ('vegetables', 0.7383119463920593), ('medicines', 0.7366275787353516)
time.sleep(10)