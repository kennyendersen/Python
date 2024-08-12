sexo = str(input('Informe seu sexo? [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos. Por favor, Informe seu Sexo: [M/F] ')).strip().upper()
print(f'\033[1;4;32mSexo {sexo} registrado com sucesso\033[m')