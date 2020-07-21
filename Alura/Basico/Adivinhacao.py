import random


def jogar():
    print('#################################')
    print('Bem vindo ao jogo de adivinhação!')
    print('#################################')
    print()

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou: ', chute)

        if chute < 1 or chute > 100:
            print('Você deve digitar um numero entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você ACERTOU e fez {} pontos!'.format(pontos))
            break
        else:
            if maior:
                print('Você ERROU! Tente um número menor\n')
                if rodada == total_de_tentativas:
                    print('O numero secreto era {}. Você fez {} pontos'.format(numero_secreto, pontos))
            elif menor:
                print('Você ERROU! Tente um número maior\n')
                if rodada == total_de_tentativas:
                    print('O numero secreto era {}. Você fez {} pontos'.format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)  # valor absoluto, módulo
            pontos -= pontos_perdidos

        rodada = rodada + 1

    print('\nEND GAME')


if __name__ == '__main__':
    jogar()
