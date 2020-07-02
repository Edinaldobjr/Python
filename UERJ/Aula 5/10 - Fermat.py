def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print('“Holy smokes, Fermat was wrong!')
        else:
            print('“No, that doesn’t work.”')
    else:
        print('N needs be higher than 2!')


pri = int(input('Digite o valor de A:'))
seg = int(input('Digite o valor de B: '))
ter = int(input('Digite o valor de C: '))
quar = int(input('Digite o valor de N: '))

check_fermat(pri, seg, ter, quar)
