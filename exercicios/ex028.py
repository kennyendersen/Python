from random import randint
from time import sleep
pc = randint(0, 5)  #Computador pensa no numero
print('Vou pensar em um numero entre 0 e 5. Tente Adivinhar...')
player = int(input('Em que numero eu pensei: ')) #Jogador tenta adivinhar o numero
print('\033[1;4;34mPROCESSANDO...\033[m')
sleep(2)
if player == pc:
    print('\033[1;4;31mPARABENS, VOCE GANHOU!\033[m')
else:
    print('\033[1;4;32mGANHEI! O numero que pensei foi o {}\033[m' .format(pc))
