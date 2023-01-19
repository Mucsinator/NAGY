def LNKO(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print('LNKO kivonásos algoritmussal')
a = int(input('a = '))
b = int(input('b = '))
print(f'LNKO({a}, {b}) = {LNKO(a,b)}') 