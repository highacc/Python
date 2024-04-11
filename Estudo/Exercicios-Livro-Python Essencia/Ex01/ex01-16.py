#Exercicio 1.16 - Crie um programa que peça ao usuário para digitar a massa e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a força resultante.

massa = float(input("Valor da Massa: "))
acel = float(input("Aceleração: "))

forca = massa * acel

print(f"A força resultante é: {forca:.2f}")