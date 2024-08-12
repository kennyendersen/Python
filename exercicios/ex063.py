print('\033[36m◊' * 23)
print('Sequencia de Fibonacci')
print('◊' * 23, '\033[m')
termo = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} → {t2}', end=' ')
while cont <= termo:
    t3 = t1 + t2
    print(f'→ {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')