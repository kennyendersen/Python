maior = 0
homem = 0
mulher = 0
while True:
    print('-'*20)
    print('\033[1;32mCADSATRE UMA PESSOA\033[m')
    idade = int(input('Idade: '))
    #verifica quantas pessoas tem mais de 18 anos
    if idade > 18:
        maior += 1
    sexo = ' '
    #ira repetir ate o usuario digitar M ou F
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    #Contagem de homens cadastrados
    if sexo == 'M':
        homem += 1
    #Contagem de mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulher += 1
    esc = ' '
    #ira repetir ate o usuario digitar S ou N
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N]')).strip().upper()
    if esc == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {homem} homens cadastrados
E temos {mulher} mulheres com menos de 20 anos''')