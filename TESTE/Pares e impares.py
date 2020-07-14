num = int(input("Digite o numero: "))

lista = list(range(1, num+1))

pares = [numero for numero in lista if numero % 2 == 0]
impares = [numero for numero in lista if numero % 2 != 0]

# print(*impares)
print(*pares, sep='\n')
