dicionario = {
    1: "a",
    2: "b",
    3: "c"
}

for chave in dicionario:
    print(chave)


for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(chave, valor)