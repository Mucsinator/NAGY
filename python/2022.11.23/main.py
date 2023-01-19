from eredmeny import Eredmeny
from typing import List

eredmenyek:List[Eredmeny]=[]

def beolvas(fajlnev):
    file=open(fajlnev, 'r', encoding="utf-8")
    for sor in file:
        eredmenyek.append(Eredmeny(sor))
    file.close()

def ermekSzama(helyezes):
    db=0
    for item in eredmenyek:
        if item.helyezes==helyezes:
            db+=1
    return db

def osszPontszam():
    osszeg=0
    for item in eredmenyek:
        osszeg+=item.pontszam()
    return osszeg

def sportagErmekSzama(sportag):
    db=0
    for item in eredmenyek:
        if item.sportag==sportag:
            db+=1
    return db

#2.feladat 
beolvas('helsinki.txt')


#3. Feladat
print("3.feladat")
print(f"Pontszerző helyezések száma: {len(eredmenyek)}")

#4. feladat
print('4. feladat:')
print(f"Arany: {ermekSzama(1)}")
print(f"Ezüst: {ermekSzama(2)}")
print(f"Bronz: {ermekSzama(3)}")
print(f"Összesen: {ermekSzama(1)+ermekSzama(2)+ermekSzama(3)}")

#5.feladat
print('5. feladat: ')
print(f'Olimpiai pontok száma: {osszPontszam()}')

#6. feladat
torna=sportagErmekSzama('torna')
uszas=sportagErmekSzama('uszas')
print("6. feladat: ")
if torna == uszas:
    print('Egyenlő volt ez érmék száma.')
elif torna > uszas:
    print('Torna sportágban szereztek több érmet.')
else:
    print("Úszás sportágban szereztek több érmet.")