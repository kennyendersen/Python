peso = float(input('Qual é seu peso? '))
altura = float(input('Qual a sua altura? '))
if altura.is_integer():
   altura = altura / 100
imc = peso / (altura * altura)
print('\033[31mO IMC dessa pessoa é de {:.1f}\033[m' .format(imc))
if imc < 16.9:
   print('\033[32mVoce esta muito abaixo do peso\033[m')
elif imc < 18.5:
   print('\033[33mVoce esta abaixo do peso\033[m')
elif imc < 25:
   print('\033[34mVoce esta no peso normal\033[m')
elif imc < 30:
   print('\033[35mVoce esta acima do peso\033[m')
elif imc < 35:
   print('\033[36mVoce esta com obesidade grau I\033[m')
elif imc < 41:
   print('\033[37mVoce esta com obesidade grau II\033[m')
else:
   print('\033[30mVoce esta com obesidade grau III\033[m')
