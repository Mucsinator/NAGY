class NobelDijas:
    Evszam=0
    Tipus=''
    Keresztnev=''
    Vezeteknev=''

    def __init__(self, sor:str):
        darabok=sor.strip().split(';')
        self.Evszam=int(darabok[0])
        self.Tipus=darabok[1]
        self.Keresztnev=darabok[2]
        self.Vezeteknev=darabok[3]
