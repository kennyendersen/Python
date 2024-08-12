velho = 0
cont = 0
soma = 0
mulher = 0
for c in range(1, 5):
    print(f'\033[36m---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    cont += 1
    soma += idade
    media = soma / cont
    if c == 1 and sexo == 'M':
        velho = idade
        nome1 = nome   
    if idade > velho and sexo == 'M':
            velho = idade
            nome1 = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
print('A media de idade do grupo e de {:.2f} anos' .format(media))
print('O homem mais velho tem {} anos e se chama {}' .format(velho,nome1))
print('Ao todo sao {} mulheres com menos de 20 anos \033[m' .format(mulher))
