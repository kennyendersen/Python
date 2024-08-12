lista = []
for cont in range(0,5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionada na posicao {pos} da lista')
                break
            pos += 1
print(lista)