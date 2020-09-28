"""
Crie uma funcão para calcular o ángulo zenital do sol (da semana passada) tomando como argumento as medidas da altura
e o comprimento da sombra.
"""


def ang_zenite(altura, sombra):
    import math
    ang = math.degrees(math.atan(sombra/altura))
    return ang


h = float(input('Defina a altura da pessoa em cm: '))
d = float(input('Defina o tamanho da sombra em cm: '))

ang = ang_zenite(h, d)

print(f'O ângulo zenital é de {ang:.2f} graus')
