#Exercicio 1.1 - Crie um programa que armazene seu nome e sua idade em variaveis separadas e imprima uma saida formatada com elas.

nome = input("Digite seu nome: ")
# O type padrão recebido pelo input é str, como mostrado pelo print da variavel idade1 
idade1 = input("Qual a sua idade1? ")
print(type(idade1))
# Como a intenção e receber um valor inteiro, para evitar erros vou converter para int como mostrado na var idade.
idade = int(input("Qual a sua idade? "))
print(type(idade))
print("Olá {}, soube que você tem {} anos.".format(nome, idade))