def is_triangle(a, b, c):
    lista = [a, b, c]
    ordem = sorted(lista)

    if ordem[0] + ordem[1] <= ordem[2]:
        print('Yes.')
    else:
        print('No.')

