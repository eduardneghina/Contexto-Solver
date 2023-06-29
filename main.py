import os
import time
from Database import *
from Extractor import *
from AI import *

def main():
    while True:
        driver = initiate_contexto()
        controller = WebController(driver)
        print("Choose an option:")
        print("1. Brute force - incearca random toate cuvintele din history ")
        print("2. Smart search (experimental) ")
        print("3. ")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            choice1_2 = input("What game number? leave empty and enter for today game: ")
            if choice1_2 == "":
                ai = AI()
                ai.try_random_noun_until_find(driver, None)
            else:
                ai = AI()
                ai.try_random_noun_until_find(driver, int(choice1_2))
        elif choice == "2":
            choice2_1 = input("What game number? leave empty and enter for today game: ")
            if choice2_1 == "":
                ai = AI()
                ai.try_smart_ish(driver, None)
            else:
                ai = AI()
                ai.try_smart_ish(driver, int(choice2_1))
        elif choice == "3":
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

