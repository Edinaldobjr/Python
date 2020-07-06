valor = float(input('Preço "Promocional": '))
ant = float(input('Preço Antigo: '))

desc = (1 - valor / ant) * 100

print('Desconto de: {:.2f} %'.format(desc))
