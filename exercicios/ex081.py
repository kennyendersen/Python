lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]')).strip().upper()
    if esc == 'N':
        break
lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')