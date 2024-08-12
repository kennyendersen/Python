r1 = int(input('Primeiro Segmento: '))
r2 = int(input('Segundo Segmento: '))
r3 = int(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('\033[1;32mOs segmentos podem formar um triangulo equilatero\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;33mOs segmentos podem formar um triangulo escaleno\033[m')
    else:
        print('\033[1;34mOs segmentos podem formar um triangulo Isosceles\033[m')
else:
        print('\033[1;35mOs segmentos nao podem formar um triangulo\033[m')