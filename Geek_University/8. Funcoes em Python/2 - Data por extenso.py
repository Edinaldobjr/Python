def conversao_mes(mes):
    """Converte meses de número para extenso."""
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro', 'Dezembro')
    dat = meses[mes-1]
    return dat


print('Escrevendo a data por extenso')

data = input('Digite a data no formato 00/00/0000: ')

d = int(data[0:2])
m = int(data[3:5])
a = int(data[-4:])

print('A data convertida é {:02d} de {} de {:4d}'.format(d, conversao_mes(m), a))
