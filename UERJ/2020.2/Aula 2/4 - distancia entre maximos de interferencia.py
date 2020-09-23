"""
Um laser vermelho (com comprimento de onda lambda = 632.8 nm) incide em uma fenda dupla produzindo um padrão de
interferência com franjas claras e escuras, em um anteparo situado a uma distância D = 1.98 m da fenda. Calcule a
distância Delta_y entre dois máximos consecutivos de interferência. Considere o espaçamento entre as fendas, $d$,
como sendo igual a 0.250 mm.
Dica: a distância entre dois máximos de interferência consecutivos pode ser aproximada por

Delta_y = (lambda * D) / d

"""
lamb = 632.8 * 10**(-9)
D = 1.98
d = 0.250 * 10**(-3)

Delta_y = (lamb * D) / d

print('A distância entre os dois máximos consecutivos de interferencia é de {} m ou de aproximadamente {:.0f} mm.'
      .format(Delta_y, Delta_y * 1000))