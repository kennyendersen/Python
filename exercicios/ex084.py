dados = []
peso = []
pessoas = maior = menor = 0
while True:
    n = str(input('nome: '))
    pessoas += 1
    p = int(input('Peso: '))
    if pessoas == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
    peso.append(p)
    dados.append(n)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]')).strip().upper()
    if esc == 'N':
        break

print(f'Voce cadastrou {pessoas} pessoas')
print(f'O maior peso foi de {maior}')
print(f'O menor peso foi de {menor}')
