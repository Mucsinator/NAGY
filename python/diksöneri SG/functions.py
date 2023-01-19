from data import *


def FajlBeolvasas():
    f=open('orvosi_nobeldijak.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        Nobeldijasok.append(Nobeldíjas(sor))
    f.close()

def UtolsóÉv():
    utolso = 0
    for i in Nobeldijasok:
        if i.Év > utolso:
            utolso = i.Év
    return utolso


def OrszagKod():
    be_orszag_kód = input('Kérem adja meg egy ország kódját: ')