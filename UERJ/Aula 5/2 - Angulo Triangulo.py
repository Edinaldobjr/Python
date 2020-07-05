def triangulo(cateto_oposto, cateto_adjacente):
    import math
    tg_theta = cateto_oposto / cateto_adjacente
    theta = math.atan(tg_theta)
    print('O ângulo correspondente é {:.2f} graus'.format(math.degrees(theta)))


x = float(input("Defina o valor do Cateto Oposto: "))
y = float(input('Defina o valor do Cateto Adjacente: '))

triangulo(x, y)
