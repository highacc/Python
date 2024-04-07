'''
print("Hello world!")

# 1-Utilizando Variáveis

nome = "Olavo"
idade = 34
peso = 70.3

print(nome, idade,peso)

#Utilizando a função input

name = input("Please enter your name: ")
age = input("Please enter your age: ")
weight = input("Please enter your weight: ")

print(name, age, weight)
'''
'''
# 2-Conversões ou CAST

name = input("Please enter your name: ")

#To convert the type of the input just call the type and use the desired input as parameter.

age = int (input("Please enter your age: "))
weight = float (input("Please enter your weight: "))

#To use variables and strings in the print function just separete them with a comma.

print("Name: ",name,"Age: ",age,"Weight: ",weight)

#Another way to use strings and functions in the print function is the f-string way.

print(f"Name: {name}, Age: {age}, Weight: {weight}")

#To get the type of the variable we call the function type(fucntionName).

print(f"Type of Name: {type(name)}, Type of Age: {type(age)}, Type of Weight: {type(weight)}")

'''
'''
# 3-Operadores Matematicos

soma = 1 + 1
subtracao = 2 - 1
multiplicacao = 2 * 2
divisao = 10 / 2
potencia = 2 ** 2

print(f"Soma: 1 + 1 = {soma}, Subtracao: 2 - 1  = {subtracao}, Multiplicacao: 2 * 2 = {multiplicacao}, Divisao: 10 / 2 = {divisao}, Potencia: 2 ** 2 = {potencia}")

'''
'''
# 4-Condicionais
#.lower() é uma funçao utilizada para converter o parametro para lower case.
# exemplo de outra forma de utilizar: name_lower = name.lower().
name = input("Digite o nome do Usuario: ").lower()

# Condicional Boolean(true or false)
administrador = ( name == "olavo")

if administrador:
    print(f"Olá, {name.capitalize()}. Você e um administrador.")
else:
    print(f"Olá, {name.capitalize()}. Infelismente você nao e um administrador.")

salario = float(input(f"Informe seu salario, {name.capitalize()}: "))

if salario <= 3000:
    print(f"{name.capitalize()}, você é um programador Junior")
elif salario > 3000 and salario <= 6000:
    print(f"{name.capitalize()}, você é um programador Pleno")
elif salario > 6000 and salario <= 15000:
    print(f"{name.capitalize()}, você é um programador Senior")
else:
    print(f"{name.capitalize()}, você é um Especialista ou Gerente de Projetos")

'''
'''
# 5-Listas ou Arrays

numeros_ar = [1, 2, 3]

print(numeros_ar)
print(numeros_ar[0])
print(numeros_ar[1])
print(numeros_ar[2])

'''
# 6-Loops
'''
notas = []

for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
print("quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)

'''

# 7- Dicionarios ou Classes(javascript) ou Structs(C)
'''
pessoa = {
    "nome" : "Programador Python",
    "idade": 34,
    "peso": 106.5
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])
'''
