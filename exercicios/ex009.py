n1 = int(input('Digite um numero para saber sua tabuada: '))
cores = { 'limpa':'\033[m',
        'magenta':'\033[1;35m',
        'ciano':'\033[1;36m',
        'blue':'\033[4;34m'
}

print(f'{cores["magenta"]}{n1}{cores["limpa"]} x {cores["blue"]}1{cores["limpa"]} = {cores["ciano"]}{n1 * 1}{cores["limpa"]}')
print(f'{cores["ciano"]}{n1}{cores["limpa"]} x {cores["blue"]}2{cores["limpa"]} = {cores["magenta"]}{n1 * 2}{cores["limpa"]}')
print(f'{cores["magenta"]}{n1}{cores["limpa"]} x {cores["blue"]}3{cores["limpa"]} = {cores["ciano"]}{n1 * 3}{cores["limpa"]}')
print(f'{cores["ciano"]}{n1}{cores["limpa"]} x {cores["blue"]}4{cores["limpa"]} = {cores["magenta"]}{n1 * 4}{cores["limpa"]}')
print(f'{cores["magenta"]}{n1}{cores["limpa"]} x {cores["blue"]}5{cores["limpa"]} = {cores["ciano"]}{n1 * 5}{cores["limpa"]}')
print(f'{cores["ciano"]}{n1}{cores["limpa"]} x {cores["blue"]}6{cores["limpa"]} = {cores["magenta"]}{n1 * 6}{cores["limpa"]}')
print(f'{cores["magenta"]}{n1}{cores["limpa"]} x {cores["blue"]}7{cores["limpa"]} = {cores["ciano"]}{n1 * 7}{cores["limpa"]}')
print(f'{cores["ciano"]}{n1}{cores["limpa"]} x {cores["blue"]}8{cores["limpa"]} = {cores["magenta"]}{n1 * 8}{cores["limpa"]}')
print(f'{cores["magenta"]}{n1}{cores["limpa"]} x {cores["blue"]}9{cores["limpa"]} = {cores["ciano"]}{n1 * 9}{cores["limpa"]}')
print(f'{cores["ciano"]}{n1}{cores["limpa"]} x {cores["blue"]}10{cores["limpa"]} = {cores["magenta"]}{n1 * 10}{cores["limpa"]}')

print('{}{}{} x {}{}{} = {}{}{}' .format(cores["blue"],n1, cores["limpa"], cores["ciano"] ,1, cores["limpa"], cores["magenta"] , n1 * 1, cores["limpa"]))