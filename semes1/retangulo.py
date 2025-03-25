lado = int(input("digite o tamanho do lado do retângulo: "))

base = int(input("digite o tamanho da base do retângulo: "))


print(lado)
print(base)

for b in range(base):
    
    for l in range(lado):
        if l == 0 or l == base -1 or b == 0 or b == base -1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()