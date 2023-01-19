class cbadás:
    def __init__(self, sor:str):
        adatok = sor.strip().split(';')
        self.Ora = int(adatok[0])
        self.Perc = int(adatok[1])
        self.AdasDb = int(adatok[2])
        self.Nev = (adatok[3])


CBadások:list[cbadás]=[]