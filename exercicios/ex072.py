cont = 21
ext = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
cont = int(input('Digite um numero entre 0 e 20: '))
while cont < 0 or cont > 20:
    cont = int(input('Tente Novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {ext[cont]}')
