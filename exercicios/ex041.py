from datetime import date
data = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = data - ano
print(f'O atleta tem {idade} anos.')
if idade < 10:
    print('\033[1;4;31mClassificacao MIRIM\033[m')
elif idade < 15:
    print('\033[1;4;32mClassificacao INFANTIL\033[m')
elif idade < 20:
    print('\033[1;4;33mClassificacao JUNIOR\033[m')
elif idade < 26:
    print('\033[1;4;34mClassificacao SENIOR\033[m')
else:
    print('\033[1;4;35mClassificacao MASTER\033[m')