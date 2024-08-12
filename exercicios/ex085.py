# par = []
# impar = []
# for c in range(1,8):
#     valor = int(input(f'Digite o {c}o. numero: '))
#     if valor % 2 == 0:
#         par.append(valor)
#     else:
#         impar.append(valor)
# print(f'Os numeros pares sao {par}')
# print(f'Os numeros impares sao {impar}')

num = [[], []]
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. numero: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os numeros pares sao {num[0]}')
print(f'Os numeros impares sao {num[1]}')