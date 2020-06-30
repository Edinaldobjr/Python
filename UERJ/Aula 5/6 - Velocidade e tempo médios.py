def mi_em_m(x):
    milhas = float(x)
    metros = (1.61 * milhas) * 1000
    return metros


def m_em_mi(x):
    metros = float(x)
    milhas = (metros * 1000) / 1.61
    return milhas


def min_em_seg(x):
    minutos = float(x)
    segundos = int(minutos * 60)
    return segundos


def seg_em_hora(x):
    segundos = int(x)
    hora = segundos * 3600
    return hora


a = input('Qual o tempo em minutos? ')
b = input('Qual a distancia em milhas? ')

velocidade = mi_em_m(b) / min_em_seg(a)
v_km = velocidade * 3.6
print('A velocidade obtida é {:.2f} km/h.'.format(v_km))

pace = seg_em_hora(min_em_seg(a))/(1000 * mi_em_m(b))
print('O tempo por quilometro é de aproximadamente {:.2f} h.'.format(pace))
