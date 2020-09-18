import numpy as np

"""
Construa a matriz que representa a métrica de Minkowski a partir de funções do numpy.
https://mathworld.wolfram.com/images/equations/MinkowskiMetric/NumberedEquation1.gif
"""
minkowski = np.eye(4)
minkowski[0][0] = -1

#m = $\eta_{\alpha\beta}$
print(f'\u03B7 \u03B1\u03B2 \u1b91 =', minkowski)
