def triangulo(x, y):
    import math

    c_o = x
    c_e = y
    tg_theta = c_o / c_e
    theta = math.atan(tg_theta)
    print('O ângulo correspondente é {:.2f} graus'.format(math.degrees(theta)))


x = float(input("Defina o valor do Cateto Oposto: "))
y = float(input('Defina o valor do Cateto Adjacente: '))

triangulo(x, y)
