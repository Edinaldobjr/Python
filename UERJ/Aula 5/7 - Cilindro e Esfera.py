def esfera(volume):
    from math import pi
    vol = volume * 10 ** 3
    raio = ((3/4) * (vol/pi)) ** (1/3)
    return raio


v_litros = float(input('Qual o volume da esfera em litros? '))

R = esfera(v_litros)

print('O raio da esfera é: {:.3f} cm'.format(R))


def cilindro(area_base, altura):
    v = area_base * altura
    return v


a_base = float(input('Qual a área da base? '))
altura = float(input('Qual a altura? '))

v = cilindro(a_base, altura)

print('O volume do cilindro é {:.3f} cm³'.format(v))
