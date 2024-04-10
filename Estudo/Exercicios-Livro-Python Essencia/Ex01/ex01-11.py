#Exercicio 1.11 - Crie um programa que peça ao usuário para digitar o raio de um círculo. Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.

import math

raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo
area = math.pi * (raio ** 2)

# Calcula o comprimento (circunferência) do círculo
comprimento = 2 * math.pi * raio

# Mostra a área e o comprimento do círculo
print("A área do círculo é: {:.2f}".format(area))
print("O comprimento do círculo é: {:.2f}".format(comprimento))