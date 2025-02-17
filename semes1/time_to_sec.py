days = int(input("Digite a quantidade de dias: "))

hours = int(input("Digite a quantidade de horas: "))

minutes = int(input("Digite a quantidade de minutos: "))

seconds = int(input("Digite a quantidade de segundos: "))

# calculation
daysToSec = (days*86400)

hoursToSec = (hours*3600)

minutesToSec = (minutes*60)

totalSec = (daysToSec+hoursToSec+minutesToSec+seconds)

# output
print(f"tempo total foi de {totalSec}")