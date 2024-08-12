cores = { 'limpa':'\033[m',
         'white':'\033[30m',
         'red':'\033[31m',
         'green':'\033[32m',
         'yellow':'\033[33m',
         'blue':'\033[34m',
         'magenta':'\033[35m',
         'ciano':'\033[36m'
}

metros = float(input('Digite uma distancia em metros: '))
print(f'A medida de {cores["blue"]}{metros}m{cores["limpa"]} corresponde a \n{cores["ciano"]}{metros / 1000}km{cores["limpa"]} \n{cores["green"]}{metros / 100}hm{cores["limpa"]} \n{cores["magenta"]}{metros / 10}dam{cores["limpa"]} \n{cores["red"]}{metros * 10:.0f}dm{cores["limpa"]} \n{cores["yellow"]}{metros * 100:.0f}cm{cores["limpa"]} \n{cores["white"]}{metros * 1000:.0f}mm{cores["limpa"]}')