from data import *
from os import system
from typing import List

nobelDijasok:List[NobelDijas]=[]

def FajlBeolvas():
    file=open('nobel.csv', 'r', encoding='utf-8')
    file.readline()
    for sor in file:
        nobelDijasok.append(NobelDijas(sor))

#-------------------
#2. feladat
FajlBeolvas()

#3. feladat
print(f"3. feladat: ", end='')
for item in nobelDijasok:
    if item.Keresztnev=='Arthur B.' and item.Vezeteknev=='McDonald':
        print(f'{item.Tipus}\n')

#4. feladat
print(f"4. feladat: ", end='')
for item in nobelDijasok:
    if item.Evszam==2017 and item.Tipus=='irodalmi':
        print(f'{item.Keresztnev} {item.Vezeteknev}\n')

#5. feladat
print(f"5. feladat: ")
for item in nobelDijasok:
    if item.Evszam>1990 and item.Vezeteknev=='':
        print(f'{item.Evszam} {item.Keresztnev}\n')

#6. feladat
print(f"6. feladat: ")
for item in nobelDijasok:
    if 'Curie' in item.Vezeteknev:
        print(f'{item.Evszam}: {item.Keresztnev} {item.Vezeteknev}({item.Tipus})')

#7. feladat
