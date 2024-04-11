#Exercicio 1.19 - Crie um programa que peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo. Em seguida, o programa deve calcular e mostrar o comprimento da hipotenusa.
import math

a = float(input("Angulo A: "))
b = float(input("Angulo B: "))

hip = math.hypot(a, b)

print("Hipotenusa: ", hip)