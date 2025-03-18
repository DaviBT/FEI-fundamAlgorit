z = 0
x = 0
notas = []
sum = 0
for z in range(0, 6):
    nota = int(input("nota: "))
    notas.append(nota)

for z in notas:
    if z >= 6: 
        x = x + 1
        
    
    sum = z + sum
print(x)
media = 0
media = sum / len(notas)
print(media)