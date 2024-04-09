#Exercicio 1.8 - Crie um programa que peça ao usuario para digitar um angulo entre 0 e 360 graus. Em seguida, o programa deve calcular e mostrar o seno, cosseno e tangente desse numero.

#Importação do modulo Math para usar funções par operações matematicas, trigonometricas, etc.
import math

angulo = int(input("Digite o angulo: "))

#Seno
seno = math.sin(math.radians(angulo))
print("Seno de", angulo, "graus: ", seno)

#Cosseno
cosseno = math.cos(math.radians(angulo))
print("Cosseno de", angulo, "graus: ", cosseno)

#Tangente
tangente = math.tan(math.radians(angulo))
print("Tangente de", angulo, "graus: ", tangente)


