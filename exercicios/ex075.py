num = tuple(int(input('Digite um numero: ')) for c in range (1,5))
nove = num.count(9)                     
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {nove} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O numero 3 nao foi digitado')
par = 0
for n in num:
    if n % 2 == 0:
        par += 1
        # print(n, end=' ')
print(f'Foram digitados {par} numero pares ')
