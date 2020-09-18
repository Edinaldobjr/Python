import matplotlib.pyplot as plt
import numpy as np

"""
Gere um distribuição Gaussiana centrada em 10 e faça o histograma da distribuição. 
(Dica: você pode usar o método np.random.normal)
"""

b = np.random.normal(size=200, loc=10, scale=3)      # Gaussiana.

plt.hist(b, bins=range(1, 20, 1))

plt.show()