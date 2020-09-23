"""
Ache os zeros da função
 y = 3 *x^2 - 4 *x -10
"""

def bhaskara(A, B, C):
    delta = (B**2-4*A*C)

    if delta > 0:
        print('Esta equação possui duas raízes reais e distintas')
        x1 = (-B + delta ** (1 / 2)) / 2 * A
        x2 = (-B - delta ** (1 / 2)) / 2 * A
        print("As raízes da equação são {} e {}".format(x1, x2))
    elif delta == 0:
        print('Esta equação possui uma raiz real')
        x1 = (-B + delta**(1/2)) / 2 * A
        print('A raiz desta equação é {}'.format(x1))
    else:
        print('Esta equação não possui raízes reais.')


print('Formula de Bhaskara\n')
print('introduza os coeficientes da equação de segundo grau:')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

bhaskara(a, b, c)
