from data import nevek,ugrások
from os import system
fajlnev = "jumps.csv"

def menu():
    system("cls")
    print("-----------MENÜ-----------")
    print("0 - Kilépés")
    print("1 - Versenyzők")
    print("2 - Eredmények")
    print("3 - Új eredmény felvétele")
    print("4 - Eredmény törlése")
    print("5 - Ugrások átlaga") #összegzés tétel
    print("6 - Győztes meghatározása") #maxkeresés tétel
    print("7 - Döntőbe kvalifikáltak listája (7.0m-nél nagyobb)") #megszámlálás tétel
    return input("Választás: ")

def fajlBetoltes():
    file=open(fajlnev,'r', encoding='utf-8')
    for sor in file:
        #sor-->Kovács Béla;7.56\n
        darabolt=sor.strip().split(';')
        nevek.append(darabolt[0])
        ugrások.append(float(darabolt[1]))
    file.close()


def versenyzok():
    system('cls')
    print("--------VERSENYZŐK--------")
    for nev in nevek:
        print(f"\t{nev}")
    input() 

def eredmenyek():
    for i in range(len(nevek)):
        print(f'\t{i+1}. {nevek[i]}: {ugrások[i]}')

def ujeredmeny():
    system('cls')
    print("-------ÚJ EREDMÉNY--------")
    bekertNev=input("Név: ")
    bekertUgras=float(input("Ugrás: ").replace(',','.'))
    ugrások.append(bekertUgras)
    nevek.append(bekertNev)
    eredmenyMentesFajlVegere(bekertNev,bekertUgras)
    input("Sikeres rögzítés")

def eredmenyMentesFajlVegere(nev, ugras):
    file = open(fajlnev,'a', encoding='utf-8')
    file.write(f'\n{nev};{ugras}')
    file.close()

def eredmenyTorlese():
    system("cls")
    print("-----EREDMÉNY TÖRLÉSE-----")
    eredmenyek()
    sSz=int(input("\nKit töröljünk?: "))
    nevek.pop(sSz-1)
    ugrások.pop(sSz-2)
    mentesFajlba()
    input('Sikeres törlés.')


def mentesFajlba():
    file=open(fajlnev, "w", encoding="utf-8")
    for i in range(len(nevek)):
        if i>0:
            file.write('\n')
        file.write(f"{nevek[i]}; {ugrások[i]}") 
    file.close()