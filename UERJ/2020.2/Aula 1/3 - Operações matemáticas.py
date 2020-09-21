"""
Inicie o interpretador Python e use-o como uma calculadora. A sintaxe do Python para operações matemáticas é quase
igual à notação matemática padrão:

adição: +
subtração: -
divisão: /
multiplicação: *

Se você fizer uma corrida de 10 quilômetros em 43 minutos e 30 segundos, qual será seu tempo médio por milha? Qual é a
sua velocidade média em milhas por hora? (Dica: há 1,61 quilômetros em uma milha).
"""
print('Distância percorrida 10 km', end=' ')
print('no intervalo de tempo de 43 min e 30 seg.')
dist_km = 10      # Distancia em Quilômetros
dist_mi = dist_km / 1.61    # Conversão de Quilômetros para Milhas

print('\nA distância é de {:.2f} milhas'.format(dist_mi), end=' ')

tempo_min = 43
tempo_seg = 30
tempo_total_hora = (tempo_min / 60) + (tempo_seg / 3600)

velocidade_milhas = dist_mi / tempo_total_hora

print('com velocidade média é de {:.2f} milhas por hora.'.format(velocidade_milhas))
