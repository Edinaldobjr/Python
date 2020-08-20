#Programa que calcula o parâmetro C para a energia ²E(²G) em um diagrama d³:

def parametro_C(dq, b, e):
    i = e / 3.05
    j = 7.90 * b / 3.05
    k = 1.80 * (b**2) / (dq * 3.05)
    c = i - j + k
    return c


if __name__ == '__main__': #permite imprimir apenas os teste sob o if, excluindo os testes
    while True:
        print('Programa que calcula o parâmetro C para a energia ²E(²G) em um diagrama d³\n'
              'Calculando o parâmetro de Racah C(cm-1):\n')
        dq = float(input('Entre com o valor de Dq: '))
        b = float(input('Entre com o valor de B: '))
        e = float(input('Entre com o valor da energia ²E: '))

        c = parametro_C(dq, b, e)

        print('\n O valor de C para os seus parametros é: {:.0f} cm-1'.format(c))

        continua = input('Deseja sair? Digite Q ou Enter para novo cálculo:').strip().upper()
        if continua == 'Q':
            break

