#Exercicio 1.18 - :: Crie um programa que peça ao usuário para digitar o valor da medida de um ângulo em radianos. Em seguida, o programa deve calcular e mostrar o valor desse ângulo em graus.
import math

radianos = math.degrees(float(input("Qual o valor da medida em radianos? ")))

print("O valor desse angulo em graus é: ", radianos)