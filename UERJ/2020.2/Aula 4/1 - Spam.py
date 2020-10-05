"""
Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam duas vezes.

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

1. Digite este exemplo em um script e teste-o.
"""


def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)

"""
2. Modifique do_twice para que sejam necessários dois argumentos, um objeto de função e um valor, e chame a função duas 
vezes, passando o valor como um argumento.
"""


def do_twice(f, palavra):
    f(palavra)
    f(palavra)


def print_spam(palavra):
    print(palavra)


nome = 'Edinaldo'

do_twice(print_spam, nome)

"""
3. Escreva uma versão mais geral de print_spam, chamada print_twice, que use uma string como parâmetro e imprima duas 
vezes.
"""


def print_twice(string):
    print(string)
    print(string)


nome = 'Edinaldo'

print_twice(nome)

"""
4. Use a versão modificada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento.
"""

nome = 'spam'
do_twice(print_twice, nome)

"""
5. Defina uma nova função chamada do_four que recebe um objeto de função e um valor e chama a função quatro vezes, 
passando o valor como um parâmetro. Deve haver apenas duas declarações no corpo desta função, não quatro.
"""


def do_four(f, palavra):
    do_twice(f, palavra)
    do_twice(f, palavra)


do_four(print_twice, nome)
