while True:
    valor = int(input('Quer ver a tabuada de qual valor (numero negativo encerra o programa)? '))
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor * c}')
print('\033[1;4;35mPrograma de Tabuada Encerrado\033[m')