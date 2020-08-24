def exponenciacao(x, y):
    multi = 1
    for _ in range(y):
        multi = multi * x
    return multi


print('\nPrograma para calcular a exponenciação de A elevado a N\n')

a = int(input('A: '))
n = int(input('N: '))

print(exponenciacao(a, n))