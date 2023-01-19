from functions import *

FajlBeolvas()
print(f'1. feladat: országok száma: {len(VBOrszagok)}')
print()
print('2. feladat: 2018-as VB csapatai:')
UtolsoVBnVolt()
print()
print(f'3. feladat: A BeNeLux országok összesen {BeNeLux()} alkalommal vettek részt a VB-n.\n')

print(f'4. feladat: Az első VB-t {ElsoVB()}-ban rendezték.\n')

print(f'5. feladat: Eddig {nyertesDb()} ország csapata volt világbajnok.\n')

print(f'6. feladat: Szarháziak legjobb eredménye: {Szarháziak()}\n')

orszag='Magyarország'
if KintVolte(orszag):
    print(f'7. feladat: {orszag} ott volt az első VB-n.\n ')
else:
    print(f'7. feladat: {orszag} nem volt ott az első VB-n.\n')

Legtobbszor()
print(f'8. feladat: legtobbszor.txt kész')