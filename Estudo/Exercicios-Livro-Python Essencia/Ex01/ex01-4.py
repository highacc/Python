#Exercicio 1.4 - Crie um programa que peça ao usuario para digitar seu peso e sua altura. Em seguida, calcule o indice de massa corporal(IMC) e imprima o resultado. A formula do IMC é: imc = peso/altura**2

print("Vamos calcular o seu indice de massa corporal(IMC)!")
peso = float(input("Qual o seu peso: "))
altura = float(input("Qual a sua altura: "))
imc = peso/altura**2

print("Seu IMC é: ", imc)