from random import random, randint

matriz = []

for linha in range(10):
    linhaM = []
    for coluna in range(5):
        num = randint(0, 100)
        linhaM.append(num)
    matriz.append(linhaM)

print(f"Matriz: \n{matriz}")

matrizTransposta = []

for linha in range(5):
    linhaM = []
    for coluna in range(10):
        linhaM.append(matriz[coluna][linha])
    matrizTransposta.append(linhaM)

print(matrizTransposta)