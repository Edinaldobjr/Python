'''
# Exercício 1
x = int(input('insira um numero inteiro: '))

y = x % 2

if y == 1:
    print('Este número é impar')
else:
    print('Esse número é par')
______________________________________________________________
# Exercício 2
x = int(input('insira um numero inteiro: '))

y = x % 3

if y == 0:
    print('Fizz')
else:
    print(x)
______________________________________________________________
# Exercício 3
x = int(input('insira um numero inteiro: '))

y = x % 5

if y == 0:
    print('Buzz')
else:
    print(x)
_______________________________________________________________
# Exercício 4
x = int(input('insira um numero inteiro: '))

y = x % 5
z = x % 3

if y == 0 and z == 0:
    print('FizzBuzz')
else:
    print(x)
_______________________________________________________________
# Exercício 5
x = float(input('insira o primeiro numero: '))
y = float(input('insira o segundo numero: '))
z = float(input('insira o terceiro numero: '))

if x < y < z:
    print('crescente')
else:
    print('não está em ordem crescente')
_______________________________________________________________
'''