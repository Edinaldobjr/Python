x = int(input('insira um numero inteiro: '))

y = x % 5
z = x % 3

if y == 0 and z == 0:
    print('FizzBuzz')
else:
    print(x)