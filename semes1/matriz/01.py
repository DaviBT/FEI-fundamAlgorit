from random import random, randint
matriz = []

linha0 = []
linha1 = []
linha2 = []
linha3 = []
linha4 = []
linha5 = []
linha6 = []
linha7 = []
linha8 = []
linha9 = []

x = 0

for coluna in range(15):
    x = randint(0, 100)
    linha0.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha1.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha2.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha3.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha4.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha5.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha6.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha7.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha8.append(x)
for coluna in range(15):
    x = randint(0, 100)
    linha9.append(x)


matriz = [linha0, linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9]

print(matriz)

print(matriz[0])