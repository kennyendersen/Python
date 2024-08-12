soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} numeros pares é igual a: \033[1;3;4;32m{soma}\033[m')