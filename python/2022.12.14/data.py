class VBOrszag:
    def __init__(self, sor:str):
        adatok=sor.split(";")
        self.Orszag=adatok[0]
        self.Reszvetel=int(adatok[1]) 
        self.Elso=int(adatok[2]) 
        self.Utolso=int(adatok[3])
        self.Eredmeny=adatok[4]

from typing import List
VBOrszagok:List[VBOrszag]=[]