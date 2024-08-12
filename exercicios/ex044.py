# TABELA DE PAGAMENTOS
# A VISTA DINHEIRO - 10% DE DESCONTO
# A VISTA NO CARTAO - 5% DE DESCONTO
# EM 2X NO CARTAO DE - PRECO NORMAL
# 3X OU MAIS NO CARTAO - 20% DE JUROS

print('\033[1;4;35m='*10, 'Loja Endersen', '=' * 10 , '\033[m')
preco = float(input('Qual o preco das compras: R$')) 
print('Formas de Pagamento')
print('[1] a vista pix/dinheiro')
print('[2] a vista cartao')
print('[3] 2x no cartao')
print('[4] 3x ou mais no cartao')
pag = int(input('Digite a opcao de pagamento: '))

if pag == 1:
    valor = preco - (preco * 0.10)
    print(f'\033[32mSua compra de R${preco:.2f} vai custar R${valor:.2f} com os 10% de desconto por pagar a vista\033[m')
elif pag == 2:
    valor = preco - (preco * 0.05)
    print(f'\033[33mSua compra de {preco:.2f} vai custar R${valor:.2f} com os 5% de desconto por pagar a vista no cartao\033[m')
elif pag == 3:
    valor = preco / 2
    print(f'\033[34mO total da sua compra sera de 2x de R${valor:.2f} sem juros no cartao\033[m')
elif pag == 4:
    parcelas = int(input('Quantas parcelas: '))
    if parcelas > 2:
        valor = preco + (preco * 0.20)
        mes = valor / parcelas
        print(f'\033[35mSua compra sera parcelada em {parcelas}x de R${mes:.2f} com juros')
        print(f'Sua compra de {preco:.2f} vai custar R${valor:.2f} no final.\033[m')
    else:
        print(f'\033[1;31mPara parcelas de 1 ou 2 vezes e necessario escolher a primeira ou segunda forma de pagameto\033[m')
else:
    print('\033[1;31mERRO! Por favor escolha uma opcao de pagamento valida\033[m')