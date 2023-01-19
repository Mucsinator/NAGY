class Épület:
    def __init__(self, sor:str):
        adatok=sor.strip().split(';')
        self.nev=adatok[0]
        self.varos=adatok[1]
        self.orszag=adatok[2]
        self.magassag=float(adatok[3].replace(',','.'))
        self.emelet=int(adatok[4])
        self.epult=int(adatok[5])

from typing import List

epuletek:List[Épület]=[]