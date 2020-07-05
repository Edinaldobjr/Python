def velocidade_final(aceleração, tempo_decorrido):
    v = aceleração * tempo_decorrido
    print('A velocidade final é de {:.2f} m/s.'.format(v))


x = float(input('Defina o valor da aceleração: '))
y = float(input('Defina o valor do tempo decorrido: '))

velocidade_final(x, y)
