print('\033[36m⇓ ' * 10 , '')
print(' 10 Termos de PA')
print('⇑ ' * 10 , '')

termo = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
for c in range(1,11):    
    print(termo, end=' → ')
    termo += razao
print('ACABOU\033[m')