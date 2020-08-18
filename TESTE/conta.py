import math

m = 9.10938e-31
me = m * 0.2
mh = me * 1.5
kb = 1.3807e-23
pi = math.pi
hcort = 1.05457e-34
t = 300
eg = 1.60218e-19

a = (me * mh) ** (3/4)
b1 = kb / (2 * pi * hcort ** 2)
b = b1**(3/2) * t ** (3/2)

# n = 2 * a * b * math.exp(-eg / (2 * kb * t))
n = 2 * a * b * math.exp(-eg / (2 * kb * t))

print('final', n)