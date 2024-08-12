valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado! nao vou adicionar')
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]')).upper().strip()
    if esc == 'N':
        break
valores.sort()
print(f'voce digitou os valores {valores}')
