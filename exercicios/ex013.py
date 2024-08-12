salario = float(input('Qual seu salario? R$'))
novo = salario + (salario * 0.15 )
print(f'Com o aumento de \033[4;36m15%\033[m, o seu salario passou a ser \033[4;35m{novo:.2f}\033[m')