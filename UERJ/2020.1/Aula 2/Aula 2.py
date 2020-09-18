"""
1. Escreva a palavra "OI " 250 vezes e imprima na tela. Dica: use o operador '*'

print('Oi '*250)

2. Considere as sílabas da palavra "Banana" separadas e concatene-as para formar a palavra impressa na tela;

frase = 'banana'

a = frase[0:2]
b = frase[2:4]
c = frase[4:]

print('Uns dizem:',a*2+b)
print('Outros falam:',b*3)
print('Alguns pensam:',c+a+b)
print('mas todas sabemos que o certo é:',a+b+c)


3. Faça um algoritmo que tome como entrada uma palavra fornecida pelo
usuário através do terminal e imprima a primeira e última letra e o
número total de letras da palavra. Dica: você pode usar as funções
'input' e 'len' e os índices da palavra.

p = input("Digite a palavra desejada: ")

str = 'Essa palavra possui {0} como letra inicial, {1} como ultima letra e pussui {2} letras.'
print(str.format(p[:2].upper(), p[-2:].upper(), len(p)))
"""