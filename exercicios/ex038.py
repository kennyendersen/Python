n1 = float(input('Primeiro Numero: '))
n2 = float(input('Segundo Numero: '))
if n1 > n2:
    print('\033[1;35mO primeiro numero é maior!\033[m')
elif n2 > n1:
    print('\033[1;34mO Segundo numero é maior!\033[m')
else:
    print('\033[1;36mOs valores sao iguais!\033[m')