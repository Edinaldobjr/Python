#    8. Crie uma lista chamada nested_list que contenha como um de seus elementos a lista minha_lista, acesse o item 'banana' em nested_list e imprima a palavra na tela;
minha_lista = ['banana', 15.4, 8, True]
"""
nested_list = [20, 'abacaxi']

nested_list += minha_lista

print(nested_list[2])
_________
"""
nested_list = [20, 'abacaxi']

nested_list.append(minha_lista)

print(nested_list)
print(nested_list[2])
print(nested_list[2][0])
print(nested_list[2][0][2:4])

if "banana" in minha_lista:
    print(locals(banana))