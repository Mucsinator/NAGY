class Nobeldíjas:
    def __init__(self, sor:str):
        adatok = sor.strip().split(';')
        self.Év = int(adatok[0])
        self.Név = adatok[1]
        self.SzülHalál = adatok[2]
        self.Országkód = adatok[3]

Nobeldijasok:list[Nobeldíjas]=[]