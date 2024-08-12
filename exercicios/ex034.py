salario = float(input('\033[1;31mQual seu salario? '))
if salario < 1251:
    salario = salario * 0.15 + salario
    print('\033[1;35mO seu novo salario sera de \033[1;4;33mR${:.2f} reais\033[m' .format(salario))
else:
    salario = salario * 0.10 + salario 
    print('\033[1;4;36mO seu novo salario sera de \033[1;4;32mR${:.2f} reais\033[m' .format(salario))
