class Szakasz:
    def __init__(self, sor:str):
        adatok = sor.strip().split(';')
        self.Indulas = adatok[0]
        self.Erkezes = adatok[1]
        self.Tavolsag = float(adatok[2].replace(',','.'))
        self.Emelkedes = int(adatok[3])
        self.Lejtes = int(adatok[4])
        self.PecseteloHely = (adatok[5]=='i')

from typing import List

szakaszok:List[Szakasz]=[]
