valor = float(input('Preço "Promocional": '))
ant = float(input('Preço Antigo: '))

dif = valor / ant

desc = (1 - dif) * 100

print('Desconto de:',desc,'Porcento')