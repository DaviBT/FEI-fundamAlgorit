import random

dicionario = {}
qtd = 0
for i in range(100):
    n = random.randint(0, 20)
    if n not in dicionario:
        dicionario[n] = 1
    else:
        dicionario[n] += 1

for chave, valor in sorted(dicionario.items()):
    print(f'{chave:02d} : {valor:02d}')