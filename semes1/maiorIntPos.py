nums = []

# nums.append(int(input("insira um numero: ")))
# nums.append(int(input("insira um numero: ")))
# nums.append(int(input("insira um numero: ")))
# nums.append(int(input("insira um numero: ")))
# nums.append(int(input("insira um numero: ")))
# nums.append(int(input("insira um numero: ")))

# print(nums)

# i = 0
# x = 0
# bigger = 0

# while i <= len(nums):
#     if x > nums[i]:
#         bigger = x
#     elif x > nums[i]:
#         x = nums[i]
    
#     i += 1


maior = 0
for x in range(6):
    n = int(input("numero: "))
    if n > maior:
        maior = n

print(maior)