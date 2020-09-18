def ang_zenite(altura, sombra):
    import math
    ang = math.degrees(math.atan(sombra/altura))
    return ang


h = float(input('Defina a altura da pessoa: '))
d = float(input('Defina o tamanho da sombra: '))

print('O ângulo zenital é de {:.2f} graus'.format(ang_zenite(h, d)))
