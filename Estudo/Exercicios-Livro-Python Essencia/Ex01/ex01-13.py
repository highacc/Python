#Exercicio 1.13 - Crie um programa que peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, o programa deve calcular e mostrar a área desse triângulo.
# Area = 1/2 * b * a

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

area = 0.5 * base * altura  

print("Area to triangulo:", area)