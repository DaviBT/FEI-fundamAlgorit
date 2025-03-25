n = int(input("Digite a quantidade de linhas: "))

for i in range(n + 1):
    if i == 0:
        continue

    for j in range(4):
        if j == 0:
            continue
        print(i ** j, end=" ")
    print()

