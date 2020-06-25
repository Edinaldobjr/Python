h = float(input('Digite sua altura em metros: '))

print('\nQual seu sexo?')
print('Digite (M) para masculino ou (F) para feminino')
sexo = input()

if sexo == 'm' or sexo == 'M':
    peso = (72.7 * h) - 58
    print('Seu peso ideal é:', peso)
else:
    peso = (32.1 * h) - 44.7
    print('Seu peso ideal é:', peso)
