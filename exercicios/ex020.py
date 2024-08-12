from random import shuffle
n1 = str(input("Primeiro nome: "))
n2 = str(input('Segundo Nome: '))
n3 = str(input('Terceiro Nome: '))
n4 = str(input('Quarto Nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será \n \033[36m{}\033[m' .format((lista)))