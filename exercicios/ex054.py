from datetime import date
data = date.today().year
menor = 0
maior = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? ' .format(c)))
    if (data - ano) < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade' .format(maior))
print('E tambem tivemos {} menores de idade' .format(menor))
