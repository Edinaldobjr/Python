import matplotlib.pyplot as plt
import numpy as np

"""
1. Graficar as funções y1 = x , y2 = x**2 e y3 = x**3, para os seguintes passos:
ok - x tenha 21 pontos no intervalo [0, 2]
ok - y1 seja uma linha azul tracejada
ok - y2 seja representada por bolinhas e verde
ok - y3 seja representada por triângulos amarelos
ok - identifique os eixos x e y
- apresente uma legenda para as três funções
"""

x = np.linspace(0, 2, 21)

plt.plot(x, x, 'b--', label='Gráfico de x = y')         # Traços Azuis
plt.plot(x, x**2, 'go', label='Gráfico de x = y²')      # Bolas Verdes
plt.plot(x, x**3, 'y^', label='Gráfico de x = y³')      # Triângulos Amarelos

plt.title('Gráficos')               # Título da Imagem
plt.xlabel('Valores em X')          # Label do Eixo x
plt.ylabel('Valores em Y')          # Label do Eixo y

# plt.axis([0, 2, -0.5, 10])
plt.ylim(-0.5, 10)
plt.xlim(0, 2)

'''
plt.annotate('y = x³', xy=(1.8, 6), xytext=(1, 9), arrowprops=dict(facecolor='yellow', shrink=0.05))
plt.annotate('y = x²', xy=(1.8, 3.2), xytext=(1, 7), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('y = x', xy=(1.8, 1.7), xytext=(1, 5), arrowprops=dict(facecolor='blue', shrink=0.05))
'''

plt.legend(loc='upper left')
plt.show()
