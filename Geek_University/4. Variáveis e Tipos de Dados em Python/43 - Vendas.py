valor = float(input('Digite o valor do produto: '))

desconto = valor * 0.9
parcelado = valor / 3
comissao_a_vista = desconto * 0.05
comissao_a_prazo = valor * 0.05

print('O valor do produto com o desconto é:', round(desconto, 2))
print('O valor do produto parcelado em 3x é:', round(parcelado, 2))
print('A comissão do vendedor com pagamento a vista:', round(comissao_a_vista, 2))
print('A comissão do vendedor com pagamento a prazo:', round(comissao_a_prazo, 2))
