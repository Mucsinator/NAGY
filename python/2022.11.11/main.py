from functions import menu, fajlBetoltes, versenyzok, eredmenyek, ujeredmeny, eredmenyTorlese
from os import system

fajlBetoltes()


valasztas = ''
while valasztas != '0':
    valasztas = menu()
    if valasztas == "1":
        versenyzok()

    elif valasztas == '2':
        system('cls')
        print("--------EREDMÉNYEK--------")
        eredmenyek()
        input()
    elif valasztas == '3':
        ujeredmeny()
    elif valasztas == '4':
        eredmenyTorlese()
