from data import *
from typing import List


def fajlBeolvas():
    f = open('orvosi_nobeldijak.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        nobeldijasok.append(nobelDij(sor))
    f.close()

def max_Ev():
    maxev = 0
    for nobeldijas in nobeldijasok:
        if nobeldijas.Ev > maxev:
            maxev = nobeldijas.Ev
    return maxev

def be_orszag_kod():
    beOrszagKod = input('Kérem az ország kódot: ')
    db = 0
    for nobeldijas in nobeldijasok:
        if nobeldijas.Orszagkod == beOrszagKod:
            db += 1
            jo_nobeldijas = nobeldijas
    
    if db == 0:
        print('\tA megadott országból nem volt díjazott')
    elif db > 1:
        print(f'\tA megadott országból {db} fő díjazott volt')
    else:
        print('\tA megadott ország díjazottja')
        print(f'\tNév: {jo_nobeldijas.Nev}')
        print(f'\tÉv: {jo_nobeldijas.Ev}')
        print(f'\tSz-H: {jo_nobeldijas.SzületesHalalozas}')

def Statisztika():
    stat = {}
    for item in nobeldijasok:
        # if item.Orszagkod != 'DK':
        if item.Orszagkod in stat.keys():
            stat[item.Orszagkod] += 1
        else:
            stat[item.Orszagkod] = 1
    # képernyőre
    for key, value in stat.items():
        if value > 5:
            print(f'\t{key} - {value} fő')
    # fajlba
    f = open('stat.txt', 'w', encoding='utf-8')
    for key, value in stat.items():
        if value > 5:
            f.write(f'{key} - {value} fő\n')
    f.close()