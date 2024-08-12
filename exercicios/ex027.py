n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é \033[1;4;33m{}\033[m' .format(nome[0]))
print('Seu ultimo nome é \033[1;4;35m{}\033[m' .format(nome[len(nome)-1]))
