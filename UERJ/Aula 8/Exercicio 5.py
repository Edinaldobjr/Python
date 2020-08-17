import numpy as np

"""
Reproduza a matriz mostrada abaixo na ilustração de indexação e fatiamento e imprima seus valores na tela. Em seguida, 
reprouduza as operações mostradas na figura e verifique os resultados. Estão todos corretos? Se não, quais não estão?
(https://scipy-lectures.org/_images/numpy_indexing.png)
"""

matriz = np.array([[ 0,  1,  2,  3,  4,  5],
                   [10, 11, 12, 13, 14, 15],
                   [20, 21, 22, 23, 24, 25],
                   [30, 31, 32, 33, 34, 35],
                   [40, 41, 42, 43, 44, 45],
                   [50, 51, 52, 53, 54, 55]])
print(f'Matriz principal:\n{matriz}')

primeira = matriz[0, 3:5]       # linha 0, coluna 3 e 5.
print(f'\nPrimeiro slice a[0, 3:5]:\n{primeira}')

segunda = matriz[4:, 4:]        # linha 4 em diante, coluna 4 em diante.
print(f'\nSegundo slice a[4:, 4:]:\n{segunda}')

terceira = matriz[:, 2]         # tudo, coluna 2.
print(f'\nTerceiro slice a[:, 2]:\n{terceira}')

quarta = matriz[2::2, ::2]      # linha 2 em diante de 2 em 2, todas as colunas de 2 em 2.
print(f'\nQuarto slice [2::2, ::2]:\n{quarta}')
