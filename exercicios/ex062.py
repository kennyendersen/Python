print('Gerador de PA')
print('='*20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao do PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais  = int(input('Quantos voce quer mostrar a mais? [0] para parar '))
print('FIM')
print('Progressao finaliza com {} termos' .format(total))
