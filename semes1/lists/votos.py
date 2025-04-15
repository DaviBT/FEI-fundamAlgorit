
votos = [0,0,0,0,0,0,0]
i = 0
numeros = []


while True:
    num = int(input('escreva um número de 1 a 6; se quiser sair o programa digite 0: '))

    if num > 6:
        continue

    if 0 < num <= 6:
        if num == 1: 
            votos[1] = votos[1] + 1
        if num == 2: 
            votos[2] = votos[2] + 1
        if num == 3: 
            votos[3] = votos[3] + 1
        if num == 4: 
            votos[4] = votos[4] + 1
        if num == 5: 
            votos[5] = votos[5] + 1
        if num == 6: 
            votos[6] = votos[6] + 1

    if num == 0:
            break




print(f'{'Sistema Operacional':<20}{' ':3}{'Votos':8}{' ':3}{'%':6}')
print(f'{'-':*20:<25}{'-'*5:6}{'-'*3:<6}')

print(f'{'Windows Server':<25}{votos[1]:8}')

# print(f'Unix: {votos[2]}')
# print(f'Linux: {votos[3]}')
# print(f'Netware: {votos[4]}')
# print(f'Mac OS: {votos[5]}')
# print(f'Outro: {votos[6]}')






