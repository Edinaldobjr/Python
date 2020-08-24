def soma_serie(n):
    soma = 0
    for x in range(1, n+1):
        s = (x**2 + 1) / (x + 3)
        soma = soma + s
    return soma


a = int(input('Qual o número: '))

print(soma_serie(a))