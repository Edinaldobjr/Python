def asterriscos(n):
    for x in range(0, n):
        print("*" * x)
    for x in range(n, 0, -1):
        print("*" * x)


a = int(input('Qual o número: '))

asterriscos(a)