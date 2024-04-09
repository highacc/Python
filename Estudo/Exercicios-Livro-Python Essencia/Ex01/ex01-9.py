#Exercicio 1.9 - Crie um programa que peça ao usuario para digitar dois numeros quaisquer. Em seguida, o programa deve calcular e mostrar a potencia do primeiro numero pelo segundo.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))

potencia = num1 ** num2

print("Potencia de {} por {} é: {}".format(num1, num2, potencia))