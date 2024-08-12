num = int(input('Digite um numero: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[35m', end='')
    print(c, end=' ')
print(f'\n\033[36mO numero {num} foi dividido {tot} vezes\033[m')
if tot == 2:
    print('O numero e primo')
else:
    print('Nao e primo')
