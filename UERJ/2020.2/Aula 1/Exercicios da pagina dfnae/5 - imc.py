"""
Calcule o seu IMC = M / A**2 (com a massa em Kg e a altura em metros). Um valor saudável estara --em geral--
entre 20-25. Um bebê de 6 meses "gorducho" tem 70 cm de "comprimento" e 11 kg de massa, qual o IMC dele?
"""
altura = 0.70        # metros
massa = 11           # quilogramas

imc = massa / altura ** 2

if 20 <= imc <= 25:
    print(f'O IMC é de {imc:.2f} que está saudável.')
elif imc < 20:
    print(f'O IMC é de {imc:.2f} que está magro.')
else:
    print(f'O IMC é de {imc:.2f} que está obeso.')