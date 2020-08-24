import math


def fatorial(n):
    fat = 1
    for x in range(1, int(n) + 1):
        fat = fat * x
    return fat


def seno_serie(x):
    soma = 0
    for n in range(0, int(x) + 1):
        s = ((-1) ** n / fatorial(2 * n + 1)) * x ** (2 * n + 1)
        soma = soma + s
    return soma


ang = int(input("Defina o angulo: "))

a = math.radians(ang)

print(seno_serie(a))
