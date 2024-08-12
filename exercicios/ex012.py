preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 0.05)
print(f'O produto que custava \033[32mR${preco}\033[m, na promoção com desconto de \033[31m5%\033[m vai custar \033[33mR${novo:.2f}\033[m')
