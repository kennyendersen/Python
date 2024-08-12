casa = float(input('Valor da casa: R$')) # Valor da casa
salario = float(input('Seu salario: R$')) # Valor do salario
anos = int(input('Quantos anos de financiamento? ')) # Anos de financiamento
salario30 = salario * 0.30 # Valor dos 30% do salario
mensal = casa / (anos * 12) # Valor da prestacao
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}' .format(casa, anos, mensal))
if salario30 >= mensal:
    print('Emprestimo Concedido!')
else:
    print('Emprestimo Negado! ')