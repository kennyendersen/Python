celsius = float(input('Informe a temperatura em C°: '))
fahr = celsius * 1.8 + 32
print('A temperatura de {}{}°C{} corresponde a {}{}°F{}!' .format('\033[4;33m',celsius, '\033[m', '\033[4;35m' ,fahr, '\033[m'))