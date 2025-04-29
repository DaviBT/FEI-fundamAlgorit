from random import randint

notas = []

for i in range(10):
    aluno = 0
    for j in range(3):
        aluno.append(randint(0,10))
    notas.append(aluno)

for aluno in notas:
    for nota in aluno:
        print(f"{nota:2d}", end=' ')
    print()

for aluno in notas:
    menorNota = min(aluno)
    prova = aluno.index(menorNota)
    print(f"menor nota: {menorNota}, prova: {prova}")


# transpor matriz de notas
notasTransposta = []
for j in range(3):
    prova = []
    for i in range(10): 
        prova.append(notas[i][j])
    notasTransposta.append(prova)

