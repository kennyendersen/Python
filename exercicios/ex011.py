largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de \033[33m{}\033[mx\033[36m{}\033[m e sua área é de \033[31m{}m²\033[m' .format(largura, altura, area))
print('Para pintar essa parede, voce precisara de {}{}{}l de tinta' .format('\033[35m' ,tinta, '\033[m'))