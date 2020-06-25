comp = float(input('Digite o comprimento do terreno: '))
larg = float(input('Digite a largura do terreno: '))
preco = float(input('Digite o preço do metro: '))

valor = (2 * comp + 2 * larg) * preco

print(round(valor, 2))
