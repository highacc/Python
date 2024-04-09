#Exercicio 1.5 - Crie um programa que peça ao usuario para digitar tres numeros e imprima a soma do dobro de cada um deles.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = int(input("Digite o numero 3: "))

num1_dobro = num1*2
num2_dobro = num2*2
num3_dobro = num3*2

soma = num1_dobro + num2_dobro + num3_dobro

print("A soma dos dobros dos numeros recebidos é: ", soma)