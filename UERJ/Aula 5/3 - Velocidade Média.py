def velocidade_media(posição_inicial, posição_final, tempo_decorrido):
    p_inicial = posição_inicial
    p_final = posição_final
    tempo = tempo_decorrido
    vm = (p_final - p_inicial) / tempo
    print('A velocidade média é de {:.2f} m/s'.format(vm))


i = float(input('Posição inicial (m): '))
f = float(input('Posição final (m): '))
t = float(input('Tempo decorrido (s): '))

velocidade_media(i, f, t)
