idade = int(input('\nDigite sua idade: '))
ano_atual = int(input('Digite o ano atual: '))
aniv = input('Você ja fez aniversário esse ano? ')

nascimento = ano_atual - idade

if aniv == 'sim' or aniv == 's':
    print('\nVocê nasceu em ', nascimento)
else:
    print('\nVocê nasceu em ', nascimento - 1)
