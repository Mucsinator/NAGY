from adat import *
from typing import List

hegyekLista:List[Hegy]=[]


#2. feladat
def FajlBeolvas():
    file=open('hegyekMo.txt','r',encoding='utf-8')
    file.readline()
    for sor in file:
        hegyekLista.append(Hegy(sor))
    file.close()


#4. feladat
def AtlagMagassag():
    ossz=0
    for hegy in hegyekLista:
        ossz+=hegy.Magassag
    return ossz

#5. feladat
def Legmagasabb():
    maxHegy=hegyekLista[0]  #a teljes példányt beletesszük
    for hegy in hegyekLista:
        if hegy.Magassag>maxHegy.Magassag:
            maxHegy=hegy
    return maxHegy

#6. feladat
def BekertEllenorzes():
    bekertMagassag=int(input('6. feladat: Kérek egy magasságot: '))
    van=False
    for hegy in hegyekLista:
        if hegy.Magassag>bekertMagassag:
            print(f'\tVan {bekertMagassag} m-nél magasabb hegycsúcs a(z) {hegy.Nev}')
            van=True
            break
    if van == False:
        print(f'Nincs {bekertMagassag} m-nél magasabb hegycsúcs! ')

#7. feladat
def HaromezernelMagasabb():
    db=0
    for hegy in hegyekLista:
        if hegy.Magassag*3.280839895>3000:
            db+=1
    return db

#8. feladat
def Statisztika():
    stat={}
    for hegy in hegyekLista:
        if hegy.Hegyseg in stat.keys():
            stat[hegy.Hegyseg]+=1
        else:
            stat[hegy.Hegyseg]=1
    for key, value in stat.items():
        print(f'\t{key}: {value} db')