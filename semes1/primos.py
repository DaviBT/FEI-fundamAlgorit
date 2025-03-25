qntNums = int(input("digite a quantidade de números a serem testados: "))

contador = 0

primos = 0
for i in range(qntNums):
    n = int(input("insira o número: "))
    if n > 1:
        ehPrimo = True
        for j in range(2, n):
            if n % j == 0:
                ehPrimo = False
                print(f"o numero {n} não é primo")
        if ehPrimo == True:
            primos = primos + 1
            print(f"o numero {n} é primo")

print(f"quantidade de números primos é {primos}")