import time

from WebController import *
from Database import *

driver_web = initiate_contexto()
controller = WebController(driver_web)
time.sleep(3)
controller.click_desired_previous_games(40);
time.sleep(3)
controller.insert_random_word()
time.sleep(3)
#looks fine so far


#let's test the db
connection = Database()
print(connection.fetch_all())
connection.close()