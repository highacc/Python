#Exercicio 1.14 - Crie um programa que peça ao usuário para digitar o nome, o preço de custo, o preço de venda e a quantidade em estoque de determinado produto. Em seguida, o programa deve calcular e mostrar o lucro que esse produto pode gerar se todo o estoque for vendido.

produto = input("Digite o nome do produto: ")
p_custo = float(input("Digite o preço de custo: "))
p_venda = float(input("Digite o preço de venda: "))
quant_estoque = int(input("Digite a quantidade de unidades em estoque: "))

lucro = (p_venda * quant_estoque) - (p_custo * quant_estoque)

print("O produto: {}, pode gerar um lucro de {}, caso todo o estoque seja vendido".format(produto, lucro))