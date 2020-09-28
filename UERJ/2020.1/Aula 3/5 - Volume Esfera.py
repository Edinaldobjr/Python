#   5.Qual deve ser o valor do raio de uma esfera, r, em centímetros, para que ela tenha um volume equivalente a um litro? Dicas: volume de uma esfera =  43πr3 ; considere a raiz cúbica de r como sendo  r1/3 . Na sintaxe de Python: r**1/3

import math

V_litros = 1
Vol = V_litros * 10 ** 3

# V = 4/3*math.pi*r**3

R = ((3/4)*(Vol/math.pi))**(1/3)

print('O raio da esfera é: {:7.3f} cm'.format(R))

"""
{:f} = float, 
{:d} = inteiro, 
{:07.2f} preencher com 0 até 7 casas total contando com a virgula e arredondar para duas casas apos a virgula 
preenchendo com zero se precisar.

print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()}')
"""