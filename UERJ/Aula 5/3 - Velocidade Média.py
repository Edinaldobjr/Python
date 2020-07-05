def velocidade_media(posição_inicial, posição_final, tempo_decorrido):
    vm = (posição_final - posição_inicial) / tempo_decorrido
    print('A velocidade média é de {:.2f} m/s'.format(vm))


i = float(input('Posição inicial (m): '))
f = float(input('Posição final (m): '))
t = float(input('Tempo decorrido (s): '))

velocidade_media(i, f, t)
