from functions import *


FajlBeolvasas()

print('3. feladat: CB-Rádió')

print(f'3.2 feladat: Bejegyzések száma: {len(CBadások)}')

print(f'3.3 feladat: Sanyihoz tartozó bejegyzések: {Sanyi()} db')

print('3.4 feladat: A legtöbb adás:')
for item in CBadások:
    if item.AdasDb==LegtöbbAdás():
        print(f'\tIdő: {item.Ora}:{item.Perc} Darab: {item.AdasDb} Név: {item.Nev}')


FajlbaIras()