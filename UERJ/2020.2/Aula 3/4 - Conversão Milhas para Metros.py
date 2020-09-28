def mi_em_m(milhas):
    metros = (1.61 * float(milhas)) * 1000
    return metros


def m_em_mi(metros):
    milhas = (float(metros) / 1000) / 1.61
    return milhas


print('Deseja converter -Metros para milhas (1)- ou -Milhas para Metros (2)- ?')
a = input('Digite a opção (1) ou (2) :').strip()

if a == '1':
    b = input('Qual a distancia em metros? ')
    print(f'A distancia {b} m convertida em milhas é de: {m_em_mi(b):.4f} mi.')

elif a == '2':
    b = input('Qual a distancia em milhas? ')
    print(f'A distancia {b} mi convertida em metros é de: {mi_em_m(b):.0f} m.')

else:
    print('Erro: Digite a opção correta.')