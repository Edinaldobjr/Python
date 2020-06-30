print('Programa para cálculo de Comissão\n')
mensal = float(input('Informe o valor de sua venda mensal: '))

if mensal >= 100000:
    comissao = 700 + mensal * .16
    print('A comissão do vendedor é R$ {:.2f}'.format(comissao))
elif mensal >= 80000:
    comissao = 650 + mensal * .14
    print('A comissão do vendedor é R$ {:.2f}'.format(comissao))
elif mensal >= 60000:
    comissao = 600 + mensal * .14
    print('A comissão do vendedor é R$ {:.2f}'.format(comissao))
elif mensal >= 40000:
    comissao = 550 + mensal * .14
    print('A comissão do vendedor é R$ {:.2f}'.format(comissao))
elif mensal >= 20000:
    comissao = 500 + mensal * .14
    print('A comissão do vendedor é R$ {:.2f}'.format(comissao))
else:
    comissao = 400 + mensal * .14
    print('A comissão do vendedor é R$ {:.2f}'.format(comissao))
