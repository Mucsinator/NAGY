from functions import *

FajlBeolvas()
print(f'3. feladat: Városok száma: {len(varosokLista)} db')

print(f'4. feladat: indiai nagyvárosok lakosságának összege: {IndiaiLakosok()} fő')

print(f'5. feladat: A legnagyobb város adatai:')
print(f'\tNév: {varosokLista[LegnagyobbVaros()].Nev}')
print(f'\tOrszág: {varosokLista[LegnagyobbVaros()].Orszag}')
print(f'\tLakosság: {varosokLista[LegnagyobbVaros()].Lakossag} ezer fő')

print(f'6. feladat: {MagyarKeres()}')

print(f'7. feladat: Városok egy szóközzel: {EgySzokoz()} db')

print(f'8. feladat: Ország statisztika')
StatKeszit()

#9
FajlbaIras()


