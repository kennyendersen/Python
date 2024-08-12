lista = []
impar = []
par = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    esc = ' '
    while esc not in 'sn':
        esc = str(input('Quer continuar? [S/N]')).strip().lower()
    if esc == 'n':
        break
print(f'A lista completa e {lista}')
print(f'A lista de numeros pares e {par}')
print(f'A lista de numeros impares e {impar}')
