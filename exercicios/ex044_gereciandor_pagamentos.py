# Exercício 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print("\033[1;32m" + "           LOJAS OHLIPEH              " + "\033[m")

print("\033[1;33m" + "         SISTEMA DE PAGAMENTO         " + "\033[m")

preco = float(input("Digite o preço do produto: R$ "))
print("Formas de pagamento:")
print("\033[1;34m" + "[ 1 ] à vista dinheiro/cheque" + "\033[m")
print("\033[1;34m" + "[ 2 ] à vista cartão" + "\033[m")
print("\033[1;34m" + "[ 3 ] 2x no cartão" + "\033[m")
print("\033[1;34m" + "[ 4 ] 3x ou mais no cartão" + "\033[m")
opcao = int(input("Escolha a forma de pagamento (1-4): "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print("Pagamento à vista no dinheiro/cheque. Você recebe 10% de desconto.")
    print(f"O valor final do produto é R$ {total:.2f}.")

elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print("Pagamento à vista no cartão. Você recebe 5% de desconto.")
    print(f"O valor final do produto é R$ {total:.2f}.")

elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Pagamento em 2x no cartão. Não há desconto ou juros.")
    print(
        f"O valor final do produto é R$ {total:.2f}, dividido em 2 parcelas de R$ {parcela:.2f}."
    )

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    num_parcelas = int(input("Quantas parcelas? "))
    parcela = total / num_parcelas
    print("Pagamento em 3x ou mais no cartão. Há um acréscimo de 20%.")
    print(
        f"O valor final do produto é R$ {total:.2f}, dividido em {num_parcelas} parcelas de R$ {parcela:.2f}."
    )

else:
    total = preco
    print("Opção inválida de pagamento. Tente novamente.")
    print(f"O valor do produto permanece R$ {total:.2f}.")
