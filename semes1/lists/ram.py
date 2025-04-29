from random import random, randint

x = 0
i = 0

inteiros = []

while i < 10:
    x = randint(0, 10)
    inteiros.append(x)
    i = i + 1

i = 0
x = 0
reais = []

while i < 5:
    x = randint(0, 100)
    reais.append(x)
    i = i + 1

strings = ["a", "b", "c", "d", "e", "f", "g"]

lisUnica = []
lisUnica = [inteiros, reais, strings]

print(lisUnica)