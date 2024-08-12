viagem = float(input('Em Km qual a distancia de sua viagem? '))
if viagem > 200:
    preco = viagem * 0.45
    print('\033[1;35mO preco de sua viagem sera de \033[1;31mR${:.2f} reais\033[m' .format(preco))
else:
    preco = viagem * 0.50
    print('\033[1;32mO preco de sua viagem sera de \033[1;36mR${:.2f} reais\033[m' .format(preco))