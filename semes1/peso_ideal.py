import math
altura = float(input("Informe sua altura atual: "))

pesoIdeal = (72.7 * altura) - 58
pesoIdeal = math.ceil(pesoIdeal)


print(f"seu peso ideal é: {pesoIdeal}")