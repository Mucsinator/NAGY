from functions import *


FajlBeolvasas()
print(f'3.2 feladat: Épületek száma: {len(epuletek)} db')

print(f'3.3 feladat: Emeletek összege: {EmeletOsszeg()}')


print('3.4 feladat: A legmagasabb épület adatai')
print(f'\tNév: {epuletek[Legmagasabb()].nev}')
print(f'\tVáros: {epuletek[Legmagasabb()].varos}')
print(f'\tOrszág: {epuletek[Legmagasabb()].orszag}')
print(f'\tMagasság: {epuletek[Legmagasabb()].magassag} m')
print(f'\tEmelet: {epuletek[Legmagasabb()].emelet}')
print(f'\tÉpült: {epuletek[Legmagasabb()].epult}')


if Olasz():
    print('3.5 feladat: Van olasz épület az adatok között!')
else:
    print('3.5 feladat: Nincs olasz épület az adatok között!')
