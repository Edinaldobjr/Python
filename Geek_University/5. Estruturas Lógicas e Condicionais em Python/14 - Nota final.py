nota_1 = float(input("Digite a nota do trabalho de laboratório: "))
if nota_1 < 0 or nota_1 > 10:
    print("Nota invalida!")
else:

    nota_2 = float(input("Digite a nota da avaliação semestral: "))
    if nota_2 < 0 or nota_2 > 10:
        print("Nota invalida!")
    else:

        nota_3 = float(input("Digite a nota do exame final: "))
        if nota_3 < 0 or nota_3 > 10:
            print("Nota invalida!")
        else:

            nota = round((nota_1 * 2 + nota_2 * 3 + nota_3 * 5) / 10, 1)
            print('Sua nota final é: {:.1f}'.format(nota))