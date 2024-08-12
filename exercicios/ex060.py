from math import factorial
n1 = int(input('Digite um numero inteiro: '))
fa = factorial(n1)
c = n1
while c > 0:
    print(c, 'x' ,end=' ')
    c -= 1
print(' = ',fa)
