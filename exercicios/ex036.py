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
