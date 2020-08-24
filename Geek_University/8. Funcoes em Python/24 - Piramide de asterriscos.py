def piramide_asteriscos(n):
    for x in range(0, n):
        b = "*" * (2*x-1)
        print(b.center(2*n-1))


a = int(input('Qual o número: '))

piramide_asteriscos(a)