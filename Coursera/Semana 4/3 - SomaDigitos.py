# Receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.

n = int(input('Digite o valor de n: '))
r = s = soma = 0

while n != 0:
    s = n // 10
    r = n % 10
    soma = soma + r
    n = s

print(soma)
