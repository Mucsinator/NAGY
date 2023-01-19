from adat import *

def FajlBeolvasas():
    f=open('cb.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        CBadások.append(cbadás(sor))
    f.close()


def Sanyi():
    db = 0
    for i in CBadások:
        if i.Nev == 'Sanyi':
            db += 1
    return db


def LegtöbbAdás():
    max = 0
    for i in CBadások:
        if i.AdasDb>max:
            max = i.AdasDb
    return max


def FajlbaIras():
    f=open('cb2.txt', 'w', encoding='utf-8')
    f.write('Kezdes;Nev;AdasDb\n')
    for item in CBadások:
        f.write(f'{item.Ora*60+item.Perc};{item.Nev};{item.AdasDb}\n')
    f.close()