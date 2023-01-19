def MghSzam(szo):
    db=0
    for i in range(len(szo)):
        if szo[i] in mgh:
            db+=1
    return db

napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
mgh = 'aáeéiíoóöőuúüű'

maxDb=0
maxPoz=0
for i in range(len(napok)):
    if MghSzam(napok[i])>maxDb:
        maxDb=MghSzam(napok[i])
        maxPoz=i

print(f'A legtöbb magánhangzó a {napok[maxPoz]}-ben van!')