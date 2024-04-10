#Exercicio 1.12 - Crie um programa que peça ao usuário para digitar as dimensões de um retângulo (largura e altura). Em seguida, o programa deve calcular e mostrar a área e o perímetro desse retângulo.
# Area do retangulo = l x a           Perimetro = 2l + 2a
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = largura * altura
perimetro = (2*largura) + (2*altura)

print("Area: ", area, "Perimetro: ", perimetro)
