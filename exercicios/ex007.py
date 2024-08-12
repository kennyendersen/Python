nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
res = (nota1 + nota2) / 2
print(f'A media entre \033[36m{nota1}\033[m e \033[32m{nota2}\033[m e igual a \033[35m{res:.1f}\033[m')

print('A media entre {}{}{} e {}{}{} e igual a {}{:.1f}{}' .format('\033[33m',nota1,'\033[m','\033[31m',nota2,'\033[m','\033[34m',res,'\033[m'))