nota = float(input('Quanto dinheiro voce tem em sua carteita? R$'))
print('Com \033[35mR${:.2f}\033[m voce pode comprar \033[36mUS${:.2f}\033[m' .format(nota, (nota / 5.43)))