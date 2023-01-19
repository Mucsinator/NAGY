class Adat:
    def __init__(self, sor):
        adatok=sor.strip().split(';')
        self.Ev=adatok[0]
        self.Nev=adatok[1]
        self.Vegyjel=adatok[2]
        self.Rendszam=int(adatok[3])
        self.Felfedezo=adatok[4]
        