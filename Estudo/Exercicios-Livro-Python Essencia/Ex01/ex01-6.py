#Exercicio 1.6 - Crie um programa que peça ao usuario para digitar um numero. Em seguida, o programa deve calcular e mostrar a raiz quadrada desse numero.

numero = int(input("Digite um numero: "))
raiz = numero ** 0.5

print("A raiz quadrada de {} é : {}".format(numero, raiz))