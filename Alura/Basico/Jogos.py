from Basico import Adivinhacao, Forca

print('#################################')
print('######Escolha o seu jogo!########')
print('#################################')
print()
print('(1) Forca (2) Advinhação')

jogo = int(input('Qual o jogo? '))

if jogo == 1:
    print('Jogando Forca')
    Forca.jogar()
elif jogo == 2:
    print('Jogando adivinhação')
    Adivinhacao.jogar()
