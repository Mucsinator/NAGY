from functions import *

FajlBeolvas()

#3. feladat
print(f'3. feladat: Hegycsúcsok száma: {len(hegyekLista)} db')

#4. feladat
print(f'4. feladat: Hegycsúcsok átlagos magassága: {AtlagMagassag()/len(hegyekLista)}')

#5. feladat
print(f'5. feladat: Legmagasabb hegycsúcs adatai:\n\tNév: {Legmagasabb().Nev}\n\tHegység: {Legmagasabb().Hegyseg}\n\tMagasság: {Legmagasabb().Magassag} m')

#6. feladat
BekertEllenorzes()

#7. feladat
print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {HaromezernelMagasabb()}')

#8. feladat
print('8. feladat: Hegység statisztika')
Statisztika()