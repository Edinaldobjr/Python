nome = input('Digite o nome do cliente: ')
dia = input('Digite o dia de vencimento: ')
mes = input('Digite o mês de vencimento: ')
valor = input('Digite o valor da fatura: ')

print('Olá, {}. A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.'.format(nome, dia, mes, valor))