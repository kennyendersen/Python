n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))
res = n1 + n2
cores = { 'limpa':'\033[m',
         'magenta':'\033[35m',
         'ciano':'\033[36m',
         'red':'\033[1;31m'
}

print('A soma entre {}{:.0f}{} e {}{:.0f}{} é igual a {}{:.0f}{}!' .format(cores['magenta'], n1, cores['limpa'], cores['ciano'], n2, cores['limpa'], cores['red'], res, cores['limpa']))