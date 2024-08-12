numero = int(input('Digite um numero entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Unidade:\033[36m{}\033[m \nDezena:\033[35m{}\033[m \nCentena:\033[34m{}\033[m \nMilhar:\033[33m{}\033[m' .format(unidade, dezena, centena, milhar))

""" numero = str(input('Digite um numero entre 0 e 9999: '))
print(numero)
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print('Unidade:{} \nDezena:{} \nCentena:{} \nMilhar:{}' .format(unidade, dezena, centena, milhar)) """