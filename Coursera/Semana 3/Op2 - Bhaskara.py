# Formula de bhaskara

import math

print('Formula de bhaskara\n')

print('introduza os coeficientes da equação de segundo grau:')
A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))

delta = (B**2-4*A*C)

if delta > 0:
    print('Esta equação possui duas raízes reais e distintas')
    x1 = (-B + math.sqrt(delta)) / 2 * A
    x2 = (-B - math.sqrt(delta)) / 2 * A
    print("As raízes da equação são {} e {}".format(x1, x2))
elif delta == 0:
    print('Esta equação possui uma raiz real')
    x1 = (-B + math.sqrt(delta)) / 2 * A
    print('A raiz desta equação é {}'.format(x1))
else:
    print('Esta equação não possui raízes reais.')
