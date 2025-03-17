s = int(input("quantos segundos você quer?"))

m =  int(input("quantos minutos você quer?"))

mshown = 0
sshown = 0
motscontator = 0

while mshown < m:
    print(f'{mshown} : {motscontator}')
    motscontator += 1
    if motscontator == 60:
        motscontator = 0
        mshown += 1

while sshown < s:
    print(f'{mshown} : {sshown}')
    sshown += 1


print(f'{m} : {s}')