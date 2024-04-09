#Exercicio 1-10 - (Difícil) Crie um programa que peça ao usuario para digitar tres numeros(A, B e C). Em seguida, o programa deve calcular e mostrar os valores das raizes da seguinte equação, usando a formula de Bhaskara: Ax**2 + Bx + C = 0.

import math

# coeficientes
a = int(input("Digite o A: "))
b = int(input("Digite o B: "))
c = int(input("Digite o C: "))

# calculando o discriminante
d = (b**2) - (4*a*c)

# verificando se as raízes são reais
if d >= 0:
    raiz1 = (-b + math.sqrt(d)) / (2 * a)
    raiz2 = (-b - math.sqrt(d)) / (2 * a)
    print("As raízes são: {} e {}".format(raiz1, raiz2))
else:
    print("As raízes são complexas")