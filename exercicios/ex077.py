tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for c in tupla:
    print(f'\nNa palavra {c} temos ', end='')
    for vogal in c:
        if vogal.upper() in 'AEIOU':
            print(vogal, end=' ')
