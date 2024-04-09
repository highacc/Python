#Exercicio 1.7 - Crie um programa que peça ao usuario para digitar um numero inteiro. Em seguida, o programa deve calcular e mostrar o valor dos inteiros anterior e posterior a esse numero.

numero = int(input("Digite um numero inteiro: "))
ant = numero - 1
post = numero + 1

print(ant, numero, post)