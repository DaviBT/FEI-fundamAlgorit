matriz = []
soma = 0

for linha in range(3):
    linhaM = []
    for coluna in range(3):
        num = int(input(f"insira um numero [{linha}], [{coluna}]: "))
        linhaM.append(num)
    matriz.append(linhaM)

print(matriz)

somaDiagonal = 0

for i in range(3):
    somaDiagonal = soma + matriz[i][i]

print(f"A soma da diagonal é: {somaDiagonal}")