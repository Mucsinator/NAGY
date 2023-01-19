from data import *

def FajlBeolvasas():
    file=open('legmagasabb.txt', 'r', encoding='utf-8')
    file.readline()
    for sor in file:
        epuletek.append(Épület(sor))
    file.close()

def EmeletOsszeg():
    osszeg = 0
    for i in epuletek:
        osszeg+=i.emelet
    return osszeg


def Legmagasabb():
    maxPoz=0
    for i in range(len(epuletek)):
        if epuletek[i].magassag>epuletek[maxPoz].magassag:
            maxPoz=i
    return maxPoz


def Olasz():
    for i in epuletek:
        if i.orszag == 'Olaszország':
            return True
    return False