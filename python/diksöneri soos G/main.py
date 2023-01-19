from functions import *


FajlBeolvasas()

print(f'3. feladat: Díjazottak száma: {len(Nobeldijasok)} fő')

print(f'4. feladat: Utolsó év: {UtolsóÉv()}')

be_orszag_kod = input('5. feladat: Kérem adja meg egy ország kódját: ')
db = 0
for nobel_dijas in Nobeldijasok:
    if nobel_dijas.Országkód == be_orszag_kod:
        db += 1
        jo_nobeldijas = nobel_dijas


if db == 0:
    print('A megadott országból nem volt díjazott!')
elif db > 1:
    print(f'A megadott országból {db} fő díjazott volt!')
else:
    print(f'\tA megadott ország díjazottja: ')
    print(f'\tNév: {jo_nobeldijas.Név}')
    print(f'\tÉv: {jo_nobeldijas.Év}')
    print(f'\tSZ/H: {jo_nobeldijas.SzülHalál} ')


Statisztika = {}


for nobel_dijas in Nobeldijasok:
    if nobel_dijas.Országkód in Statisztika:
        Statisztika[nobel_dijas.Országkód] += 1
    else:
        Statisztika[nobel_dijas.Országkód] = 1

for key, value in Statisztika.items():
    if value > 5:
        print(f'{key} - {value} fő')