print('Gerador de PA')
print('='*20)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razao do PA: '))
totermo = (razao * 9) + termo
while termo < totermo:
    print(termo, end=' → ')
    termo += razao
print(totermo, '→ FIM')