import time
from Database import *
from Extractor import *
from AI import *
import argparse

def main():
    while True:
        driver = initiate_contexto()
        controller = WebController(driver)
        print("Choose an option:")
        print("1. ")
        print("2. ")
        print("3. ")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()