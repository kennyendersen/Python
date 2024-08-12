n1 = int(input('Digite um numero inteiro: '))
c = n1
f =1
for c in range(c , 0, -1):
    print(c ,end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)