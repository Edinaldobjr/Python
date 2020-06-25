"""
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if idade < 12:
    print("Você é uma criança.")
elif idade >= 12 and idade <= 18:
    print("Você é um adolescente.")
elif idade > 18 and idade <= 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
"""
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if idade > 60:
    print("Você é um idoso.")
elif idade > 18:
    print("Você é um adulto.")
elif idade > 12:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")
