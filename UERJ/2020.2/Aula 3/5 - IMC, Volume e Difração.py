import math


def volume_esfera(raio):
    volume = 4/3*math.pi*raio**3
    return volume


def imc(massa, altura):
    imc = massa / altura ** 2
    return imc


def difracao(lamb, distancia, fenda):
    delta_y = (lamb * distancia) / fenda
    return delta_y


# Esfera
r = 5
print(f'O volume da esfera é de {volume_esfera(r):.2f} cm³.')


# IMC
a = 0.70        # metros
m = 11          # quilogramas

print(f'O IMC é de {imc(m, a):.2f} que está na região saudável.')


# Difração
l = 632.8 * 10 ** (-9)     # em manometros
dist = 1.98
d = 0.250 * 10 ** (-3)        # em milimetros

print(f'A distância entre os dois máximos consecutivos de interferencia é de {difracao(l, dist, d)} m '
      f'ou aproximadamente {difracao(l, dist, d) * 1000:.0f} mm.')