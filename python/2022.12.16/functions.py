from adat import *

def FajlBeolvas():
    file=open('kektura.csv','r',encoding='utf-8')
    kiinduloMagassag=int(file.readline())
    for sor in file:
        szakaszok.append(Szakasz(sor))
    file.close()
    return kiinduloMagassag


def TeljesHossz():
    összeg = 0
    for i in szakaszok:
        összeg += i.Tavolsag
    ossztav = str(round(összeg,3))
    return ossztav.replace('.',',')

def LegrövidebbSzakasz():
    legkisebb = szakaszok[0]
    for i in szakaszok:
        if i.Tavolsag < legkisebb.Tavolsag:
            legkisebb.Tavolsag = i.Tavolsag
    return legkisebb