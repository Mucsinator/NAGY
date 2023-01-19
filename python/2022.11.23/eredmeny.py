class Eredmeny:
    def __init__(self, sor:str):
        adatok=sor.strip().split(' ') #feldarabolja a fájl egy sorát
        self.helyezes=int(adatok[0])
        self.letszam=int(adatok[1])
        self.sportag=adatok[2]
        self.versenyszam=adatok[3]

    def pontszam(self):    #helyezésből pontszám előállítása
        pont=7-self.helyezes
        return pont+1 if self.helyezes==1 else pont