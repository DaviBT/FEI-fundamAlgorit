linhas = int(input("diga o lado do quadrado: "))
colunas = linhas
for l in range(linhas):

    for c in range(colunas):
        if c >= l:
            print("x", end=" ")
        elif c < l:
            print("o", end=" ")
    print()