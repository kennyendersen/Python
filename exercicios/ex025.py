nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome possui Silva? \033[31m{}\033[m'.format('SILVA' in nome.upper()))