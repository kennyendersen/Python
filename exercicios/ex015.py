dias = int(input('Quantos dias foi alugado? '))
km = int(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de \033[4;36mR${total}\033[m')