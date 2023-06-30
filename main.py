import os
import time
from Database import *
from Extractor import *
from AI import *

# Project created for InfoAcademy Python course - Neghina Eduard - Python 79

# Buna ziua si sper sa va placa proiectul meu la fel de mult cum mi-a placut mie prima sedinta cu selenium si cum mereu mi-am dorit sa fac asta dar nu stiam de unde sa incep.

########## !!! ########## !!! ########## !!! ########## !!! ########## !!! ########## !!!
# ~~~ RECOMANDARE : DESCHIDERE IN IDE ~~~
# mai multe pachete precum gensim.downloader / selenim / etc sunt necesare pentru buna functionare instalarea lor fiind foarte usoara de aici
##############################################################################################################################################

# Contexto-Solver este o aplicatie console care poate incerca sa rezolve cuvantul secret din jocul https://contexto.me/
# https://contexto.me/ - in fiecare zi cuvantul secret se schimba, cuvantul de pe locul 1 este cuvantul secret
# Se incearca cuvinte contextuale pana ajungem la rezultat. Mai putine incercari = mai bine !
# Aplicatia are 3 optiuni precum : forta bruta ( incearca top 25.000 words din istoricul contexto ) [ vezi extracted_data_example.txt]
# o functie "inteligenta" unde daca lista de cuvinte returnate de AI se afla deja in topul cuvintelor gasite atunci incearca alte 10 cuvinte random din cele 25.000 de mai sus
# astfel, creste sansa sa lovit un cuvant mai apropiat de cuvantul secret, iar lista returnata de AI o sa fie diferita - vezi ai.py linia 79
# Nu s-au folosit multe lucruri folositoare pentru fine-tuning deoarece necesita timp mult si foarte multa putere de procesare ( cu RTX3050 dura ore bune ) precum NTLK
# Modelul din AI este de forma Word2Vec dar si BERT sau ELMo si-ar fi facut treaba
# Nu s-a folosit Mittens sau NLTK pentru fine-output precum doar nouns sau most used words care ar fi strans mult aria de cautare, but is there for future.
# Am incercat sa scriu fiecare metoda/functie ca sa fie super usor de citit tot codul
# Scuze daca l-am trimis prea tarziu, am fost extra-ordinar de ocupat si l-am inceput acum 3 zile.
# La job am inceput o automatizare in python unei aplicatii wpf cu pywinauto si cu siguranta acest curst m-a ajutat
# Multumesc !
def main():
    while True:
        driver = initiate_contexto()
        controller = WebController(driver)
        print("Choose an option:")
        print("1. Brute force - incearca random toate cuvintele din history ")
        print("2. Smart search (experimental) ")
        print("3. Get the secret word by giving up")
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
            choice3_1 = input("What game number? leave empty and enter for today game: ")
            if choice3_1 == "":
                pass
            else:
                ai = AI()
                print("The secret word for game number " + str(choice3_1) + " was")
                print(ai.give_up_and_return_the_word(driver, int(choice3_1)))
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

