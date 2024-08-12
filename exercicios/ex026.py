frase = str(input('Escreva qualquer frase: ')).strip().upper()
print('A letra aparece \033[32m{}\033[m vezes na frase.' .format(frase.count('A')))
print('A primeira letra A apareceu na posição \033[m{}\033[m' .format(frase.find('A')+1))
print('A ultima letra "A" apareceu na posicao \033[33m{}\033[m' .format(frase.rfind('A')+1))