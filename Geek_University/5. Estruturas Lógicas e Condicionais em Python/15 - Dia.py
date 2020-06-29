dia = int(input("Digite o número do dia da semana entre 1 e 7: "))

if 1 <= dia <= 7:
    if dia == 1:
        print('Domingo')
    elif dia == 2:
        print('Segunda-Feira')
    elif dia == 3:
        print('Terça-Feira')
    elif dia == 4:
        print('Quarta-Feira')
    elif dia == 5:
        print('Quinta-Feira')
    elif dia == 6:
        print('Sexta-Feira')
    elif dia == 7:
        print('Sábado')
else:
    print('Erro 404')
