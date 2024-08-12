valores = []
maior = 0
menor = 0
posma = 0
posme = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
for c, v in enumerate(valores):
   #print(f'Na posicao {c} encontrei o valor {v}...')
    if c == 0:
        maior = menor = v
    else:
        if v > maior:
            maior = v
            posma = c
        if v < menor:
            menor = v
            posme = c
print('Cheguei ao final da lista')
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição {posma}')
print(f'O menor valor digitado foi {menor} na posição {posme}')
