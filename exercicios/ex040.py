nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno e de {media:.1f}')
if media < 5:
    print('\033[4;31mALUNO REPROVADO!!!\033[m')
elif media >= 7:
    print('\033[1;4;32mALUNO APROVADO!!!\033[m')
else:
    print('\033[1;4;33mALUNO DE RECUPERACAO!!!\033[m')