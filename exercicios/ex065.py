soma = maior = menor = cont = 0
esc = ''
while esc in 'Ss':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    esc = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('voce digitou {} numeros e a media foi {:.2f}' .format(cont, media))
print('O maior valor foi {} e o menor foi {}' .format(maior, menor))
