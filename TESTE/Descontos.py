while True:
    valor = float(input('\nPreço "Promocional": '))
    ant = float(input('Preço Antigo: '))

    desc = (1 - valor / ant) * 100

    print('Desconto de: {:.2f} %\n'.format(desc))

    x = input('Para terminar digite (Q) ').strip().upper()
    if x == 'Q':
        break
