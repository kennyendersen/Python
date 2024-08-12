vel = float(input('Qual a velocidade atual do seu carro? '))
if vel > 80:
    print('Multado! Voce excedeu o limite de velocidade que é de 80km/h')
    multa = (vel - 80) * 7
    print('Voce deve pagar uma multa de \033[1;33mR${:.2f}\033[m reais!' .format(multa))
print('\033[1;4;35mTenha um bom dia! Dirija com segurança!\033[m')
