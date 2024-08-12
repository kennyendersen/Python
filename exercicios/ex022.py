nome = str(input('Digite seu nome completo, por favor: ')).strip()
print('Seu nome em Maiúsculas é \033[32m{}\033[m' .format(nome.upper()))
print('Seu nome em Minúsculas é \033[33m{}\033[m' .format(nome.lower()))
print('Seu nome tem ao todo \033[34m{}\033[m letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem \033[35m{}\033[m letras' .format(len(nome.split()[0])))
print('Seu primeiro nome tem \033[36m{}\033[m letras' .format(nome.find(' ')))




""" upper = nome.upper()
lower = nome.lower()
letras = len(nome)
split = nome.strip()
primeiro = len(nome.split()[0])
print('Assim fica o seu nome todo em letras maiusculas:', upper)
print('Assim fica o seu nome todo em letras minusculas:', lower)
print('Essa é a quantidade de caracteres que seu nome possui', letras)
print('Essa e a quantidade de caracteres que seu primeiro nome possui', primeiro) """