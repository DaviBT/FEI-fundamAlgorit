numerosNeg = []
numerosPos = []


while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num >= 0:
            numerosNeg.append(num)
        if num <= 0:
            numerosPos.append(num)

numeros = numerosPos + numerosNeg
print(numeros)