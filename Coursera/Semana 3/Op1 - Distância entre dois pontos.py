"""
Exercício 1 - Distância entre dois pontos
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y
de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro
ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima     longe      na saída.
Caso o contrário, quando a distância for menor que 10, imprima     perto
​
"""

x = int(input("Digite a coordenada X de um ponto em um plano cartesiano: "))
y = int(input("Digite a coordenada Y de um ponto em um plano cartesiano: "))
k = int(input("Digite a coordenada X de um outro ponto no mesmo plano: "))
l = int(input("Digite a coordenada Y de um outro ponto no mesmo plano: "))

d = ((x - k)**2 + (y - l)**2)**(1/2)

if d >= 10:
    print("Longe")
else:
    print("Perto")
