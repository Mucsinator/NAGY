from varos import *
from typing import List

varosokLista:List[Varos]=[]

def FajlBeolvas():
    file=open('varosok.txt','r',encoding='utf-8')
    file.readline() #eldobjuk az első sort
    for sor in file:
        aVaros=Varos(sor)
        varosokLista.append(aVaros)
    file.close()

def IndiaiLakosok():
    osszeg=0
    for item in varosokLista:
        if item.Orszag=='India':
            osszeg+=item.Lakossag
    return osszeg*1000

def LegnagyobbVaros():
    max=varosokLista[0].Lakossag
    maxPoz=0
    for i in range(len(varosokLista)):
        if varosokLista[i].Lakossag>max:
            max=varosokLista[i].Lakossag
            maxPoz=i
    return maxPoz

def MagyarKeres():
    for item in varosokLista:
        if item.Orszag=='Magyarország':
            return 'Van magyar város az adatok között!' #ha van, akkor visszatérünk
    return 'Nincs magyar város az adatok között!'   #ha nincs, akkor visszatérünk

def EgySzokoz():
    db=0
    for item in varosokLista:
        if len(item.Nev.split(' '))==2:  #városnevet szétdarabolva, ha a 
            db+=1                        #keletkezett lista pontosan 2
    return db                            #elemű, akkor 1 szóköz van benne
                                         #akkor növeljük a db-t

def StatKeszit():
    stat={}   #dictionary
    for item in varosokLista:               #feltölti adatokkal
        if item.Orszag in stat.keys():
            stat[item.Orszag]+=1
        else:
            stat[item.Orszag]=1
    
    for key, value in stat.items():         #kiírja a dictionary-t
        if value>6:
            print(f'\t{key} - {value} db')


def FajlbaIras():
    file=open('kina.txt', 'w', encoding='utf-8')
    for item in varosokLista:
        if item.Orszag=='Kína':
            file.write(f'{item.Nev};{item.Lakossag}\n')
    file.close()