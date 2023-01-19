from data import *

def FajlBeolvasas():
    f=open('fob2016.txt', 'r', encoding='utf-8')
    for sor in f:
        versenyzok.append(Versenyzo(sor))
    f.close()

def NoiVersenyzok():
    db = 0
    for i in versenyzok:
        if i.Kategoria == 'Noi':
            db += 1
    return db/len(versenyzok)*100

def NoiBajnok():
    bajnokPoz=0
    for i in range(len(versenyzok)):
        if versenyzok[i].Kategoria=='Noi' and versenyzok[i].Osszpont()>versenyzok[bajnokPoz].Osszpont():
            bajnokPoz=i
    return bajnokPoz


def FerfiPontok():
    f=open('osszpontFF.txt', 'w', encoding='utf-8')
    for item in versenyzok:
        if item.Kategoria=='Felnott ferfi':
            f.write(f'{item.Nev};{item.Osszpont()}\n')
    f.close()

#diksöneri

def Statisztika():
    stat={}
    for item in versenyzok:
        if item.Egyesulet!='a.n.':          #n.a kizárása
            if item.Egyesulet in stat.keys():
                stat[item.Egyesulet]+=1
            else:
                stat[item.Egyesulet]=1
    
    #képernyőre
    for key, value in stat.items():
        if value>2:
            print(f'\t{key} - {value}')
    #fájlba
    f=open('statisztika.txt','w', encoding='utf-8')
    for key, value in stat.items():
        if value>2:
            f.write(f'\t{key} - {value}\n')
    f.close()