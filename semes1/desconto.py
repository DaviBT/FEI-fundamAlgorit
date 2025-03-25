valorCompra = float(input("Digite o valor da compra: "))

parcelas = int(input("Digite a quantidade de parcelas: "))

porcDesc = 0
if valorCompra > 5000:
    porcDesc = 5

if parcelas == 1:
    porcDesc = porcDesc + 10

if parcelas == 2 or parcelas == 3:
    porcDesc = porcDesc + 5

porcDesc = porcDesc / 100
valorDescontado = valorCompra * porcDesc
valorDescontadoformatado = "{:.2f}".format(valorDescontado)

print(f"Desconto total: {valorDescontadoformatado}")

valorFinal = valorCompra - valorDescontado
valorFinalFormatado = "{:.2f}".format(valorFinal)

print(f"Valor final da compra com desconto: {valorFinalFormatado}")

valorParcela = valorFinal / parcelas
valorParcelaFormatado = "{:.2f}".format(valorParcela)

print(f"Cada parcela será de: {valorParcelaFormatado}")