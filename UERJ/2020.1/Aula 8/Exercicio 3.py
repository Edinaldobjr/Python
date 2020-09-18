import numpy as np

"""
Use os métodos do numpy para definir uma matriz e tomar a sua transposta. 
(Dica: uma matriz pode ser representado como um narray. Olhe também o método T do numpy).
"""

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(f'Matriz Original:\n{matriz}')

transposta = matriz.transpose()         # matriz transposta

print(f'Matriz transposta:\n{transposta}')