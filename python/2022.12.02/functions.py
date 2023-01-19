from data import *
from typing import List

adatok:List[Adat]=[]

def FajlBeolvas():
    file=open('felfedezesek.csv', 'r', encoding='utf-8')
    file.readline()
    for sor in file:
        adatok.append(Adat(sor))
    file.close()


def OkorSzamol():
    db=0
    for item in adatok:
        if item.Ev=='Ókor':
            db+=1
    return db

def Beker():
    bekertvegyjel=''
    ok=False
    while ok==False:
        ok=False
        bekertvegyjel=input('5. feladat: Kérek egy vegyjelet: ')
        if len(bekertvegyjel)>=1 and len(bekertvegyjel)<=2:
            for betu in bekertvegyjel:
                if betu.lower()>='a' and betu.lower()<='z':
                    ok=True
                else:
                    ok=False
                    break
    return bekertvegyjel


def Kereses(vegyjel):
    van=False
    for item in adatok:
        if str(item.Vegyjel).lower()==str(vegyjel).lower():
            van=True
            print(f'\tAz elem vegyjele: {item.Vegyjel}')
            print(f'\tAz elem neve: {item.Nev}')
            print(f'\tRendszáma: {item.Rendszam}')
            print(f'\tFelfedezés éve: {item.Ev}')
            print(f'\tFelfedező: {item.Felfedezo}')
    if van==False:
        print('\tNincs ilyen elem az adatforrásban!')


def MaxEv(): 
    max=0
    for i in range(0, len(adatok)-1):
        if adatok[i].Ev!='Ókor':
            elteltEv=int(adatok[i+1].Ev)-int(adatok[i].Ev)
            if elteltEv>max:
                max=elteltEv
    return max


def Statisztika():
    stat={}
    for item in adatok:
        if item.Ev!='Ókor':
            if item.Ev in stat.keys():
                stat[item.Ev]+=1    #ha már volt akkor növeljük
            else:
                stat[item.Ev]=1     #ha nem volt akkor felvesszük új elemként

    print('8. feladat: Statisztika!')
    for key, value in stat.items():
        if value>3:
            print(f'\t{key}: {value} db')