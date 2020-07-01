def is_triangle(Lado_A, Lado_B, Lado_C):
    lista = [Lado_A, Lado_B, Lado_C]
    ordem = sorted(lista)

    if ordem[0] + ordem[1] <= ordem[2]:
        print('No.')
    else:
        print('Yes.')


print('Insira os lados do triangulo')
a = int(input('Lado A: '))
b = int(input("Lado B: "))
c = int(input('Lado C: '))

is_triangle(a, b, c)

