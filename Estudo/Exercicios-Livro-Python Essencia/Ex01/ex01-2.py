#Exercicio 1.2 - Crie um programa que armazene dois numeros em variaveis separadas e imprima a soma, subtração, multiplicação e divisão desses numeros.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("Soma = {} \nSubtração = {} \nMultiplicação = {}\nDivisão = {}".format(soma, subtracao,multiplicacao, divisao))