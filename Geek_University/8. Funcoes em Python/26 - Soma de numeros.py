def soma_numeros(n):
    soma = 0
    for x in range(1, n+1):
        soma = soma + x
    return soma


a = int(input('Qual o número: '))

print(soma_numeros(a))