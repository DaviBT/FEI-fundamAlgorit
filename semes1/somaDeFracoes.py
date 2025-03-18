z = 0
n = 0
sum = 0
while True:
    n = int(input("digita um numero: "))
    if n > 2:
        break

numero = n + 1

for z in range(2, numero):
    sum = 1 / z + sum

print(sum)