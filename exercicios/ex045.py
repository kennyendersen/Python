from random import randint
from time import sleep
print('Suas opcoes \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA')
player = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
pc = randint(1, 3)
if player == 1 and pc == 1:
    print('\033[32mComputador jogou PEDRA\033[m')
    print('\033[32mO jogador jogou PEDRA\033[m')
    print('\033[32mEMPATE!\033[m')
elif player == 1 and pc == 2:
    print('\033[33mO computador jogou PAPEL\033[m')
    print('\033[33mO jogador jogou PEDRA\033[m')
    print('\033[33mO Computador GANHOU!\033[m')
elif player == 1 and pc == 3:
    print('\033[34mO computador jogou TESOURA\033[m')
    print('\033[34mO player jogou PEDRA\033[m')
    print('\033[34mO jogador GANHOU!\033[m')
elif player == 2 and pc == 1:
    print('\033[35mO computador jogou PEDRA\033[m')
    print('\033[35mO jogador jogou PAPEL\033[m')
    print('\033[35mO jogador GANHOU!\033[m')
elif player == 2 and pc == 2:
    print('\033[36mO computador jogou PAPEL\033[m')
    print('\033[36mO jogador jogou PAPEL\033[m')
    print('\033[36mEMPATE!\033[m')
elif player == 2 and pc == 3:
    print('\033[31mO computador jogou TESOURA\033[m')
    print('\033[31mO jogador jogou PAPEL\033[m')
    print('\033[31mO computador GANHOU!\033[m')
elif player == 3 and pc == 1:
    print('\033[31mO computador jogou PEDRA\033[m')
    print('\033[31mO jogador jogou TESOURA\033[m')
    print('\033[31mO computador GANHOU!\033[m')
elif player == 3 and pc == 2:
    print('\033[32mO computador jogou PAPEL\033[m')
    print('\033[32mO jogador jogou TESOURA\033[m')
    print('\033[32mO jogador GANHOU!\033[m')
elif player == 3 and pc == 3:
    print('\033[33mO computador jogou TESOURA\033[m')
    print('\033[33mO jogador jogou TESOURA\033[m')
    print('\033[33mEMPATE!\033[m')
else:
    print('Jogada Invalida')