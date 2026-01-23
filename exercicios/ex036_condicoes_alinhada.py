## Exercício 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
    print(f"Prestação mensal será de R$ {prestacao:.2f}")
else:
    print("Empréstimo NEGADO!")
    print(f"Prestação mensal será de R$ {prestacao:.2f}")
