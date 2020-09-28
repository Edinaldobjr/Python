"""
print('O raio da esfera é: {:7.3f} cm'.format(R))

print(f'O raio da esfera é: {R:7.3f} cm')

{:f} = float, 
{:d} = inteiro, 
{:20} = imprime a string em 20 espaços,
{:<20} = imprime alinhado a esquerda
{:>20} = imprime alinhado a direita,
{:^20} = imprime centralizado,
{:=^20} = imprime centralizado com os faltantes completos de igual,
{:.2f} = arredonda em 2 casas decimais apos a virgula
{:07.2f} preencher com 0 até 7 casas total contando com a virgula e arredondar para duas casas apos a virgula 
preenchendo com zero se precisar.

print(f'O raio é: {R} cm', end='')
end = '_' = coloca um caracter no final da linha nao pulando ela.

nome = Edinaldo
print(f'Meu nome é {nome}') == Meu nome é Edinaldo
print(f'Meu nome é {nome.lower()}')

.lower() = caixa baixa
.upper() = Caixa alta
.title() = Primeira maiúscula

CTRL + F = Encontrar
CTRL + R = Substituir

.append(valor) = adiciona um valor ao final lista
.pop() = remove o ultimo valor de uma lista
.max() = pega o maior valor de uma lista
.min() = pega o menor valor de uma lista
.sorted() = ordem crescente
.sorted(reverse=True) = ordem decrescente
.clear() = limpa a lista
.strip() = remove os espaços desnecessarios em uma digitação

"""
print("cm\u0304\u00b2")
print("cm\u207b\u00b9")     # melhor
print("cm\u0304\u00b9")