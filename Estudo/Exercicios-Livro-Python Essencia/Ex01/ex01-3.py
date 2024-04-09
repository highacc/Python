#Exercicio 1.3 - Crie um programa que peça ao usuario para digitar tres numeros, armazenando-os em variveis distintas. Em seguida, imprima a média aritmetica dos tres numeros.
'''
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
media = (num1 + num2 + num3)/3

print("A média aritmetica dos tres numeros é : ", media)
'''
#Outra forma de fazer seria, nem sempre o mais dificil é melhor kkk

numeros = []
j = True
i = 0
soma = 0
while j == True:
    novo_numero = int(input("Digite o proximo numero: "))
    numeros.append(novo_numero)
    continuar = input("Quer continuar? s/n ")
    if continuar == "n":
        j = False
    
while i < len(numeros):
    soma += numeros[i]
    i += 1
media = soma/len(numeros)
print("A media é: ", media)