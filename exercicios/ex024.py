cidade = str(input('Digite o nome de uma cidade: ')).strip()
cid = cidade.upper().split()[0]
santo = cid == 'SANTO'
print('\033[35m',santo,'\033[m')