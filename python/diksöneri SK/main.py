from functions import *


FajlBeolvasas()

print(f'3. feladat: Versenyzők száma: {len(versenyzok)}')

print(f'4. feladat: A női versenyzők aránya: {round(NoiVersenyzok(),2)} %')
# print(f'4. feladat: A női versenyzők aránya: {NoiVersenyzok():.2f} %')

# print(versenyzok[39].Osszpont())

print('6. feladat: A bajnok női versenyző')
print(f'\tNév: {versenyzok[NoiBajnok()].Nev}')
print(f'\tEgyesület: {versenyzok[NoiBajnok()].Egyesulet}')
print(f'\tÖsszpont: {versenyzok[NoiBajnok()].Osszpont()}')

FerfiPontok()

print('8. feladat: Egyesület statisztika')
Statisztika()