def soma_entre(a, b):
    soma = 0
    sub = b - a
    for n in range(0, sub - 1):
        a += 1
        soma += a
    return soma


print('\nPrograma para calcular a soma de N numeros inteiros existentes entre 2 valores\n')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

print(soma_entre(num1, num2))
