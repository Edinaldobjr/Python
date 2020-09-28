"""
Crie uma função que calcule e imprima velocidade media de um objeto a partir de uma posição inicial, a final e o tempo
transcorrido para um objeto em MRU.

Também crie uma funcão que calcule e imprima a velocidade de um objeto a partir da
aceleração constante e o tempo (MRUA) (p.ex. queda libre).
"""


def velocidade_mru(posicao_inicial, posicao_final, tempo_decorrido):
    vm = (posicao_final - posicao_inicial) / tempo_decorrido
    print(f'A velocidade média em MRU é de {vm:.2f} m/s')


def velocidade_muv(aceleracao, tempo_decorrido):
    vf = aceleracao * tempo_decorrido
    print(f'\nA velocidade final em MUV é de {vf:.2f} m/s')


pos_ini = 0         # metros
pos_fin = 100       # metros
tempo = 5           # segundos

velocidade_mru(pos_ini, pos_fin, tempo)

acel = 5            # metros por segundo ao quadrado

velocidade_muv(acel, tempo)
