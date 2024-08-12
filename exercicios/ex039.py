from datetime import date
data = date.today().year
ano = int(input('Ano de nascimento: '))
idade = data - ano
print('Quem nasceu em {} tem {} anos em {}' .format(ano, idade, data))
if idade < 18:
    idade2 = 18 - idade
    print(f'Ainda faltam {idade2} anos para o alistamento')
    print(f'Seu alistamento será em {idade2 + data}.')
elif idade > 18:
    idade2 = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos' .format(idade2))
    print('Seu alistamento foi em {}' .format(data - idade))
else:
    print('Voce tem que se alistar IMEDIATAMENTE!')
