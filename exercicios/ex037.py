import math
numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das opcoes abaixo para conversao: ')
print('[1] Converter para BINARIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
print('[4] Converter para todas as opcoes')
opcao = int(input('Sua opcao: '))
lista = [bin(numero), oct(numero), hex(numero)]

if opcao == 1:
    print('{} convertido para BINARIO é igual a \033[1;4;35m{:b}\033[m' .format(numero, numero))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a \033[1;4;36m{:o}\033[m' .format(numero, numero))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[1;4;32m{:x}\033[m' .format(numero, numero))
elif opcao == 4:
    print(f'{numero} convertido para BINARIO é: \033[4;35m{numero:b}\033[m')
    print(f'{numero} convertido para OCTAL é: \033[4;36m{numero:o}\033[m')
    print(f'{numero} convertido para HEXADECIMAL é: \033[4;32m{numero:x}\033[m')
else:
    print('\033[4;31mOPCÃO INVÁLIDA!!!\033[m')