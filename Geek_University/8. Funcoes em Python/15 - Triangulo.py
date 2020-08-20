def verificar_triangulo(Lado_A, Lado_B, Lado_C):
    """Ordena os lados dados e verifica se é ou não um triangulo"""
    lista = [Lado_A, Lado_B, Lado_C]
    ordem = sorted(lista)

    if ordem[0] + ordem[1] <= ordem[2]:
        tri = False
    else:
        tri = True

    return tri


def class_lados_triangulo(Lado_A, Lado_B, Lado_C):
    if Lado_A == Lado_B == Lado_C:
        print('Equilátero.')
    elif Lado_A != Lado_B != Lado_C:
        print('Escaleno.')
    else:
        print('Isósceles.')


while True:
    a = float(input('Digite o primeiro lado: '))
    b = float(input('Digite o segundo lado: '))
    c = float(input('Digite o terceiro lado: '))

    if verificar_triangulo(a, b, c):        # Verificar se é triângulo.
        print('É um triângulo.')
    else:
        print('Não é um triângulo\n')
        continua = input('Deseja sair? Digite Q ou Enter para novo cálculo:').strip().upper()
        if continua == 'Q':
            break
        continue

    class_lados_triangulo(a, b, c)          # Classificação quanto aos lados

    continua = input('Deseja sair? Digite Q ou Enter para novo cálculo:').strip().upper()
    if continua == 'Q':
        break
