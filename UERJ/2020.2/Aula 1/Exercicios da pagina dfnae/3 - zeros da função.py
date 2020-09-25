"""
Ache os zeros da função

"""
print('Formula de Bhaskara')
print('y = 3x² - 4x - 10\n')
a = 3
b = -4
c = -10

delta = (b**2-4*a*c)

print('Esta equação possui duas raízes reais e distintas', end=' ')

x1 = (-b + delta ** (1 / 2)) / 2 * a
x2 = (-b - delta ** (1 / 2)) / 2 * a

print(f"que são {x1:.2f} e {x2:.2f}.")



