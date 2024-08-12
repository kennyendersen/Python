from random import choice
primeiro = str(input('Primeiro Nome: '))
segundo = str(input('Segundo Nome: '))
terceiro = str(input('Terceiro Nome: '))
quarto = str(input('Quarto Nome: '))
lista = [primeiro, segundo, terceiro, quarto]
sorte = choice(lista)
print(f'O nome sorteado foi \033[35m{sorte}\033[m')
              