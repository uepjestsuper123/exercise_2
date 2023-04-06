# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

# kwadrat

from cmath import pi, sqrt
from re import I


a = 10 # dlugosc bokow

obwod = a*4
pole = a*a

# obwod kwadratu wynosi 40, a pole 100.

print("Obwod kwadratu wynosi " + str(obwod) + ", a pole wynosi " + str(pole) + ".")

print(f'Obwod kwadratu wynosi {obwod}, a pole wynosi {pole}.')

# prostokat, kazdy osobny element ma byc commitnięty

c = 10 # pierwsza dlugosc bokow
d = 5 # druga dlugosc bokow

obwod_p = 2*c+2*d
pole_p = c*d

print("Obwod prostokata wynosi " + str(obwod_p) + ", a pole wynosi " + str(pole_p) + ".")

# kolo

r = 5 # dlugosc promienia

obwod_k = 2*pi*r
pole_k = pi*r*r

print("Obwod kola wynosi " + str(obwod_k) + ", a pole wynosi " + str(pole_k) + ".")

# trapez

e = 26 # dlugosc gornej podstawy
f = 16 # dlugosc dolnej podstawy
g = 13 # dlugosc bokow
h = 12 # wysokosc

obwod_t = e+f+2*g
pole_t = e*h

print("Obwod trapezu wynosi " + str(obwod_t) + ", a pole wynosi " + str(pole_t) + ".")