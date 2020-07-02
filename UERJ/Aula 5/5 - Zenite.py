def ang_zenite(altura, sombra):
    import math
    teta = math.atan(sombra/altura)
    ang = math.degrees(teta)
    return ang


h = float(input('Defina a altura da pessoa: '))
d = float(input('Defina o tamanho da sombra: '))

print('O ângulo zenital é de {:.2f} graus'.format(ang_zenite(h, d)))
