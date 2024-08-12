from random import randint
from time import sleep
pc = randint(1,10)
cont = 1
print('Sou seu computado...')
print('Acabei de pensar em numero entre 0 e 10.')
print('Consegue adivinhar qual foi? ')
player = int(input('Qual seu palpite? '))
while player != pc:
    cont += 1
    sleep(1)
    if player < pc:
        print('\033[35mMais... Tente mais uma vez.\033[m')
    if player > pc:
        print('\033[36mMenos... Tente mais uma vez.\033[m') 
    player = int(input('Qual seu palpite? '))

sleep(2)
print('\033[32mVoce acertou com {} tentativas. Parabens!\033[m' .format(cont))
