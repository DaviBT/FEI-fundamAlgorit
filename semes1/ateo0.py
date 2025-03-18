limit = 0
i = 0
z = 0
sum = 0
nums = []
media = 0
while True:
    num = int(input("coloca o numero: "))
    if num == 0:
        break
        
    else:
        nums.append(num)

qntNums = len(nums)
print(f"qnt de numeros: {qntNums}")

for z in nums:
    sum = z + sum

print(f"soma dos numeros: {sum}")

media = sum / qntNums
print(f"media dos numeros {media}")