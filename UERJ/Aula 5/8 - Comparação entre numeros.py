def comparacao(x, y):
    if x > y:
        print("{} maior do que {}".format(x, y))
    elif x == y:
        print("{} igual a {}".format(x, y))
    else:
        print("{} menor do que {}".format(x, y))


a = input('X = ')
b = input('Y = ')

comparacao(a, b)
