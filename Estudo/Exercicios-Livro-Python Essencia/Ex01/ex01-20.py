#Exercicio 1.20 - Crie um programa que peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto no trajeto. Em seguida, o programa deve calcular e mostrar a velocidade média do objeto.

distancia = float(input("Distancia percorrida: "))
t = float(input("Tempo: "))

vm = distancia / t

print("Velocidade Media: ", vm)