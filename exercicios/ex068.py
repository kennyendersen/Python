from random import randint
pc = randint(0,10)
cont = 0
print('Vamos jogar Par ou Ímpar')
while True:
    player = int(input('Digite um valor: '))
    total = pc + player
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if escolha == 'P':
        if total % 2 == 0:
            print(f'Voce jogou {player} e o computador {pc}. Total de {total} deu par')
            print('Voce ganhou')
        else:
            print(f'Voce jogou {player} e o computador {pc}. Total de {total} deu Impar')
            print('Voce perdeu')
            break
    if escolha == 'I':
        if total % 2 == 0:
            print(f'Voce jogou {player} e o computador {pc}. Total de {total} deu par')
            print('Voce perdeu')
            break
        else: 
            print(f'Voce jogou {player} e o computador {pc}. Total de {total} deu impar')
            print('Voce ganhou')
    cont += 1
print(f'\033[4;31mGamer Over! voce venceu {cont} vezes.\033[m')