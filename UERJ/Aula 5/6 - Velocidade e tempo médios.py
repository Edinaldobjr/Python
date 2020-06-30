def mi_em_m(x):
    milhas = float(x)
    metros = (1.61 * milhas) / 1000
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