#Exercicio 1.15 - Crie um programa que peça ao usuário para digitar o valor total de uma venda, o percentual de desconto aplicado e o percentual de imposto cobrado. Ao fim, o programa deve mostrar o preço final da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

venda = float(input("Valor Total da Venda: "))
desconto = float(input("Desconto: "))
imposto = float(input("Imposto: "))

valor_final = venda * (1 - desconto/100) * (1 + imposto/100)

print(f"Preço final de Venda: R$ {valor_final:.2f}")
