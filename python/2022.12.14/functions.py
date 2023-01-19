from data import *

def FajlBeolvas():
    fajl=open('fociVBk.csv','r', encoding='utf-8')
    fajl.readline()
    for sor in fajl:
        VBOrszagok.append(VBOrszag(sor))
    fajl.close()

def UtolsoVBnVolt():
    vb2018=[]
    for i in VBOrszagok:
        if i.Utolso==2018:
            vb2018.append(i.Orszag)
    for i in range(len(vb2018)):
        if i%4==0:                      #sor első eleme
            print(f'\t{vb2018[i]:14}',end='')
        elif i%4==3:
            print(f'{vb2018[i]:14}')
        else:
            print(f'{vb2018[i]:14}',end='')

def BeNeLux():
    benelux=['Belgium','Hollandia','Luxemburg']
    db=0
    for item in VBOrszagok:
        if item.Orszag in benelux:
            db+=item.Reszvetel
    return db

def ElsoVB():
    elso=VBOrszagok[0].Elso
    for item in VBOrszagok:
        if item.Elso<elso:
            elso=item.Elso
    return elso

def nyertesDb():
    db=0
    for item in VBOrszagok:
        if 'Világbajnok' in item.Eredmeny:
            db+=1
    return db

def Szarháziak():
    for item in VBOrszagok:
        if item.Orszag=='Szlovákia':
            return item.Eredmeny


def KintVolte(orszag):
    for item in VBOrszagok:
        if item.Orszag==orszag and item.Elso==ElsoVB():
            return True
    return False
    

def Legtobbszor():
    f=open('legtobbszor.txt', 'w', encoding='utf-8')
    for item in VBOrszagok:
        if item.Reszvetel>10:
            f.write(f'{item.Orszag}: {2022-item.Elso}\n')
    f.close()