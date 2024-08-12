n1 = int(input('\033[30mPrimeiro Valor: \033[m'))
n2 = int(input('\033[31mSegundo Valor: \033[m'))
n3 = int(input('\033[32mTerceiro Valor: \033[m'))
lista = [n1, n2, n3]
lista_or = sorted(lista)
print('O menor numero e \033[1;31m{}\033[m'. format(lista_or[0]))
print('O maior numero e \033[1;31m{}\033[m' .format(lista_or[2]))
