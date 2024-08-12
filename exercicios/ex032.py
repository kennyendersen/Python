from datetime import date
ano = int(input('\033[32mQue ano quer analisar? Coloque 0 o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[4;35mO ano é Bissexto\033[m')
else:
    print('\033[4;36mO ano não é bissexto\033[m')