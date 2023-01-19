import random 
import math

def ez_prím(szam):
    for i in range(2, int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True

def vaneprim():
    for item in szamok:
        if ez_prím(item):
            return 'Van prímszám a listában!'
    return 'Nincs prímszám a listában!'

szamok=[]
for i in range(10):
    szamok.append(random.randint(10,99))

print(szamok)
print(vaneprim())