dicionario = {
    'alpha': 1,
    'bravo': 2,
    'charlie': 1,
    'delta': 3,
    'echo': 1
}

def procuraChave(dicionario, valor):
    chavesEncontradas = []
    for chave, value in dicionario.items():
        if value == valor:
            chavesEncontradas.append(chave)
    return chavesEncontradas

print(procuraChave(dicionario, 1))
