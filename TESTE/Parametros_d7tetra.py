"""
Programa que calcula os parâmetros de Racah B e C e o parâmetro Dq para um sistema tetraédrico d7 (correspondente ao
diagrama de Tanabe-Sugano d3 octaédrico). Quando observada a transição:
"""


# 4T1(4P)-4A2(4F)=j e 4T1(4P)-4T2(4F)=i.


def lambda_cm1(l):
    cm = (1 / l) * 10 ** 7
    """Converte comprimento de onda em energia(cm-1)."""
    return cm


def equacao_bhaskara(i, j):
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
        x1 = (-b - delta ** (1 / 2)) / (2 * a)
        x2 = (-b + delta ** (1 / 2)) / (2 * a)
        return x1, x2
    else:
        print('Esta equação não possui valores reais para Dq.')


def calcula_b(beta):
    """ Importa o valor de beta para calcular o parametro B """
    k = lambda_cm1(beta)
    b = k / 15
    return b


def calcula_c(b):
    """ Importa o parametro B para calcular o parametro C """
    c = 4.5 * b
    return c


def calcula_dqb(dq, b):
    """ Importa os parametros Dq e B para calcular a razão Dq/B """
    dqb = dq / b
    return dqb


if __name__ == '__main__':
    while True:
        print('Calculando dos parâmetros de Racah Dq, B e C em (cm-1):\n')
        beta = float(input('Entre com o valor do comprimento de onda para a transição 4T1(4P)-4T2(4F): '))
        alfa = float(input('Entre com o valor do comprimento de onda para a transição 4T1(4P)-4A2(4F): '))

        print('\nOs valores dos comprimentos de onda são {:.0f} nm e {:.0f} nm. Os valores convertidos para energia são'
              ' respectivamente {:.0f} cm-1 e {:.0f} cm-1.'.format(alfa, beta, lambda_cm1(alfa), lambda_cm1(beta)))

        dq1, dq2 = equacao_bhaskara(beta, alfa)
        b = calcula_b(beta)
        c = calcula_c(b)
        dqb = calcula_dqb(dq1, b)

        print('\nOs valores de Dq são: {:.0f} cm-1 e {:.0f} cm-1'.format(dq1, dq2))
        print('\nO valor para o parâmetro de Racah B: {:.2f} cm-1'.format(b))
        print('\nO valor para o parâmetro de Racah C: {:.2f} cm-1'.format(c))
        print('\nO valor para o parâmetro Dq/B: {:.2f} cm-1\n'.format(dqb))

        continua = input('Deseja sair? Digite Q ou Enter para novo cálculo:').strip().upper()

        if continua == 'Q':
            break
