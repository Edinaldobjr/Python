print('Insira os lados do triangulo')
a = int(input('Lado A: '))
b = int(input("Lado B: "))
c = int(input('Lado C: '))

lista = [a, b, c]
ordem = sorted(lista)

if ordem[0] + ordem[1] <= ordem[2]:
    print('Não é um triângulo.')
else:
    print('É um triangulo', end=' ')

    if a == b == c:
        print('equilátero')
    elif a == b or a == c or b == c:
        print('isosceles')
    else:
        print('escaleno')
