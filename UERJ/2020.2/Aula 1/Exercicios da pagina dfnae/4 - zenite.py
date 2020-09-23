"""
Se, ao meiodia, a sombra de um poste de 5 m de altura tem apenas 50 cm de comprimento no chão, qual o ângulo zenital
do sol?
"""


def ang_zenite(altura, sombra):
    import math
    ang = math.degrees(math.atan(sombra/altura))
    return ang


h = float(input('Defina a altura da pessoa: '))
d = float(input('Defina o tamanho da sombra: '))

print('O ângulo zenital é de {:.2f} graus'.format(ang_zenite(h, d)))
