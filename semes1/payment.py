# input
hourPrice = float(input("digite o valor da hora de trabalho: "))
hoursWorked = float(input("digite o número de horas trabalhadas no mês: "))

# calc
totWage = hourPrice*hoursWorked

IR = 0.11
IRPart = totWage*IR

INSS = 0.08
INSSPart = totWage*INSS

UNION = 0.05
unionPart = totWage*UNION

totDeduction = IRPart+INSSPart+unionPart

liquidSalary = (totWage-totDeduction)

# output

print(f"+ Salário bruto: R${totWage}")
print(f"- IR (11%): R${IRPart}")
print(f"- INSS (8%): R${INSSPart}")
print(f"- Sindicato (8%): R${unionPart}")
print(f"+ Salário líquido: : R${liquidSalary}")







