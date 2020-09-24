"""
Suponha que o preço de um livro seja 24.95 reais, porém as livrarias têm desconto de 40%. Os custos de envio são de
3.00 reais para o primeiro livro e 0.75 reais para os livros adicionais. Qual é o custo total da compra de 60 livros?
"""
preco_livro = 24.95
desconto = 40
envio_1 = 3.00
envio_resto = 0.75
total_livros = 60

preco_compra = preco_livro * total_livros * (1 - desconto / 100)

frete = envio_1 + (total_livros - 1) * envio_resto

preco_total = preco_compra + frete

print('O preço para a compra de 60 livros é de {:.2f} Reais.'.format(preco_total))