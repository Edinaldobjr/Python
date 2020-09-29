"""
Se, ao meio dia, a sombra de um poste de 5 m de altura tem apenas 50 cm de comprimento no chão, qual o ângulo zenital
do sol?
"""
import math

h = 5
d = 0.05

ang = math.degrees(math.atan(d / h))

print(f'O ângulo zenital é de {ang:.2f} graus')
