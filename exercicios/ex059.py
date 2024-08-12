from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0

while opcao != 5:
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Numeros \n[5] Sair do programa')
    opcao = int(input('Qual sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[36mO resultado de {n1} + {n2} é {soma}\033[m')
    elif opcao == 2:
        multi = n1 * n2
        print('\033[36mA resultado de {} x {} é {}\033[m' .format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            print('\033[36mO {} é maior do que {}.\033m' .format(n1, n2))
        elif n2 > n1:
            print('\033[36mO {} é maior do que {}\033[m' .format(n2, n1))
        else:
            print('\033[36mOs valores são iguais\033[m')
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    if opcao > 5:
        print('\033[1;34;31mOpcão inválida. Tente Novamente\033[m')
    print('\033[35m=\033[m'*25)
    sleep(1)
print('\033[4;31mPrograma Finalizado\033[m')