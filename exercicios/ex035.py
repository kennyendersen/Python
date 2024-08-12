reta1 = float(input("\033[1;32mPrimeira reta: \033[m"))
reta2 = float(input("\033[1;33mSegunda reta: \033[m"))
reta3 = float(input("\033[1;34mTerceira reta: \033[m"))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[1;4;35mAs medidas acima podem formar um triangulo!\033[m')
else:
    print('\033[1;4;36mAs retas acima nao podem formar um triangulo!\033[m')