class Hegy:
    def __init__(self, sor:str):
        adatok=sor.strip().split(';')
        self.Nev=adatok[0]
        self.Hegyseg=adatok[1]
        self.Magassag=int(adatok[2])