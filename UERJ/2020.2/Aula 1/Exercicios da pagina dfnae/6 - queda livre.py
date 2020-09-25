"""
Calcule a velocidade final de um objeto em queda livre a partir de 3 metros de altura (sem resistencia do ar).
Calcule o tempo que esse objeto demora para cair.
"""
altura = 3      # metros
gravidade = 10  # metros por segundo ao quadrado

velocidade = (2 * gravidade * altura) * (1/2)

tempo = velocidade / gravidade

print(f'A velocidade final é de {velocidade} m/s e o tempo de queda é de {tempo} segundos.')
