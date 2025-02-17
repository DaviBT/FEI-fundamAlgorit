distPercorrida = float(input("digite a quantidade de quilômetros percorridos: "))
precoDist = (distPercorrida*0.15)


dias = int(input("digite a quantidade de dias que o carro foi usado: "))
precoDias = (dias*60)

totalPagar = (precoDias+precoDist)

print(f"total a pagar: R${totalPagar}")