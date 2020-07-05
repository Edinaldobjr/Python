def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print('\n“Holy smokes, Fermat was wrong!')
        else:
            print('\n“No, that doesn’t work.”')
    else:
        print('\nN needs be higher than 2!')


pri = int(input('Digite o valor de A: '))
seg = int(input('Digite o valor de B: '))
ter = int(input('Digite o valor de C: '))
qua = int(input('Digite o valor de N: '))

check_fermat(pri, seg, ter, qua)
