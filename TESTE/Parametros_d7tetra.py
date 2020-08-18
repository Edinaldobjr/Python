"""
Programa que calcula os parâmetros de Racah B e C e o parâmetro Dq para um sistema tetraédrico d7 (correspondente ao
diagrama de Tanabe-Sugano d3 octaédrico). Quando observada a transição:
"""


# 4T1(4P)-4A2(4F)=j e 4T1(4P)-4T2(4F)=i.


def lambda_cm1(l):
    cm = (1 / l) * 10 ** 7
    # converte comprimento de onda em energia(cm-1).
    return cm


def equacao_bahskara(i, j):
    k = lambda_cm1(i)
    l = lambda_cm1(j)
    a = 100
    b = 10 * k - 20 * l
    c = l ** 2 - k * l
    delta = (b ** 2 - 4 * a * c)

    if delta == 0:
        print('A equação possui apenas um valor para Dq.')
        x = (-b + delta ** (1 / 2)) / (2 * a)
        print('O valor de Dq é: ', x, 'cm-1')
        return x
    elif delta > 0:
        print('A equação possui dois valores para Dq.')
        x1 = (-b - delta ** (1 / 2)) / (2 * a)
        x2 = (-b + delta ** (1 / 2)) / (2 * a)
        print('Os valores de Dq são: ', round(x1, 0), 'cm-1', 'e', round(x2, 0), 'cm-1')
        return x1, x2
    else:
        print('Esta equação não possui valores reais para Dq.')


def calcula_b(beta):
    k = lambda_cm1(beta)
    b = k / 15
    return b


def calcula_c(beta):
    b = calcula_b(beta)
    c = 4.5 * b
    return c


if __name__ == '__main__':
    while True:
        print('Calculando dos parâmetros de Racah Dq, B e C em (cm-1):\n')
        alpha = float(input('Entre com o valor do comprimento de onda para a transição 4T1(4P)-4T2(4F): '))
        beta = float(input('Entre com o valor do comprimento de onda para a transição 4T1(4P)-4A2(4F): '))

        print()
        equacao_bahskara(alpha, beta)

        print('\nO valor para o parâmetro de Racah B: ', calcula_b(beta), 'cm-1')

        print('\nO valor para o parâmetro de Racah C: ', calcula_c(beta), 'cm-1\n')

        continua = input('Deseja sair? Digite Q ou Enter para novo cálculo:').strip().upper()
        if continua == 'Q':
            break
