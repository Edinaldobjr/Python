a = float(input('Digite a primeira nota: '))

if a < 0 or a > 10:
    print('Nota Invalida')

else:
    b = float(input('Digite a segunda nota: '))

    if b < 0 or b > 10:
        print('Nota Invalida')

    else:
        media = (a + b) / 2
        m = round(media, 1)
        print('A média é:', m)
