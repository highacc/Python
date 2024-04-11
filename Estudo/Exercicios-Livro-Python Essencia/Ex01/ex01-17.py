#Exercicio 1.17 - :: Crie um programa que peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de transição de uma velocidade para a outra. Em seguida, o programa deve calcular e mostrar a aceleração.

v1 = float(input("Velocidade inicial: "))
v2 = float(input("Velocidade final: "))
t1 = float(input("Tempo inicial: "))
t2 = float(input("Tempo final: "))

acel = (v1 - v2) / (t1 - t2)

print(f"A Aceleração resultante é: {acel:.2f}")