from math import radians, cos, sin, tan
angulo = int(input('Digite o angulo que voce deseja: '))
raio = radians(angulo)
print(f'O Angulo de \033[33m{angulo}\033[m tem o seno de \033[32m{sin(raio):.2f}\033[m')
print(f'O angulo de \033[34m{angulo}\033[m tem o cosseno de \033[35m{cos(raio):.2f}\033[m')
print(f'O angulo de \033[36m{angulo}\033[m tem a tangente de \033[31m{tan(raio):.2f}\033[m')
