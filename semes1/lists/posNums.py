qntNums = int(input('Escreva quantos números você quer verificar: '))
intervals = [0,0,0,0]
i = 0
numeros = []


while i < qntNums:
    num = int(input('escreva um número: '))
    if num not in numeros:
        numeros.append(num)

        if num >= 0 and 25 >= num:
            intervals[0] = intervals[0] + 1
        
        elif num >= 26 and 50 >= num:
            intervals[1] = intervals[1] + 1
        elif num >= 51 and 75 >= num:
            intervals[2] = intervals[2] + 1
        elif num >= 76 and 100 >= num:
            intervals[3] = intervals[3] + 1

    i = i + 1


print(f'intervalo 0-25: {intervals[0]}')
print(f'intervalo 26-50: {intervals[1]}')
print(f'intervalo 51-75: {intervals[2]}')
print(f'intervalo 76-100: {intervals[3]}')






