import numpy as np

"""
Considere o método de numpy dot e estime a multiplicação matricial das seguintes matrizes e sugira um outro exemplo de 
multiplicação matricial.

A = np.array([[3,5,6],[4,-3,8]])
B = np.array([[2,2], [-1,4], [8,6]])
"""

a = np.array([[3, 5, 6], [4, -3, 8]])
b = np.array([[2, 2], [-1, 4], [8, 6]])

print(np.dot(a, b))
print()
print(a @ b)

z = np.array([[a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0],
               a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1]],
              [a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0],
               a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1]]])

print()
print()

# k = np.array([[m, n], [o, p]])
lista = []

#for pri in range(0, len(a[0])):
#    for seg in range(0, len(b[0])):
#        m = a[pri][0] * b[0][seg] + a[pri][1] * b[1][seg] + a[pri][2] * b[2][seg]
#        lista.append(m)

# print(lista)