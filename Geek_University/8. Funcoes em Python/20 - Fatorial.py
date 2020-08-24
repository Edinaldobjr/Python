def fatorial(n):
    fat = 1
    for x in range(1, n+1):
        fat = fat * x
    return fat


print('Fatorial de um numero')
a = int(input('Qual o número: '))

print(fatorial(a))
