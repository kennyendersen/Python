from time import sleep
from math import sqrt
n1 = float(input('Digite um numero: '))
cores = { 'limpa':'\033[m',
        'magenta':'\033[1;35m',
        'red':'\033[31m',
        'verde':'\033[32m',
        'ciano':'\033[36m'
}
#print(f'O dobro de {cores['magenta']}{n1}{cores['limpa']} vale {cores['ciano']}{(n1 * 2)}{cores['limpa']}.' )

print('O dobro de {}{}{} vale {}{}{}.' .format(cores['magenta'], n1, cores['limpa'], cores['ciano'] ,(n1 * 2), cores['limpa']))
sleep(1)
print('O triplo de {}{}{} vale {}{}{}.' .format(cores['red'], n1 , cores['limpa'], cores['verde'], (n1 * 3), cores['limpa']))
sleep(1)
print('A raiz quadrada de {}{}{} vale {}{:.2f}{}' .format(cores['ciano'], n1, cores['limpa'], cores['red'], sqrt(n1) , cores['limpa'] ))
