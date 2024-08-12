from math import hypot
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(catop, catad)
print('A hipotenusa vai medir: {}{:.2f}{}' .format('\033[31m',hipo,'\033[m'))