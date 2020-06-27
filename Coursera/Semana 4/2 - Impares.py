# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.

i = int(input('Digite o valor de n: '))

for n in range(1, i*2+1):
    if n % 2 != 0:
        print(n)