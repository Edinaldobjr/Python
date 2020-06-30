def velocidade_final(aceleração, tempo_decorrido):
    a = float(aceleração)
    t = float(tempo_decorrido)

    v = a * t

    print('A velocidade final é de {:.2f} m/s.'.format(v))


x = input('Defina o valor da aceleração: ')
y = input('Defina o valor do tempo decorrido: ')

velocidade_final(x, y)
