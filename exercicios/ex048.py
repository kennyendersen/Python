import math
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'\033[4;35mA soma de todos os {cont} valores é {soma}\033[m')
