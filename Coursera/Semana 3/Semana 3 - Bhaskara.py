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
    print('X1 =', x1)
    print('X2 =', x2)
elif delta == 0:
    print('Esta equação possui uma raíz real')
    x1 = (-B + math.sqrt(delta)) / 2 * A
    print('X =', x1)
else:
    print('Esta equação não possui raizes reais')
