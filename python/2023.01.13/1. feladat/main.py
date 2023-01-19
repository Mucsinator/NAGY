import math

print('1. feladat: Háromszög kerülete és területe\nKérem a háromszög oldalait')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
K = a+b+c
print(f"K = {K}")
T = math.sqrt(K/2*(K/2-a)*(K/2-b)*(K/2-c))
print(f"T = {T}")
