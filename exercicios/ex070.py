print('Loja Kenny Endersen')
total = menor = mil = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco do produto: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print(f'''O total do compra foi R${total:.2f}
Temos {mil} produto custando mais de R$1000 reais
O produto mais barato foi {barato} que custa R${menor}''')