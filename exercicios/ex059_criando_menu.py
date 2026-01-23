# Exercício 059: Crie um programa que leia dois números e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Div
# [4] Maior
# [5] Menor
# [6] Sair do programa

from time import sleep

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opcao = 0

while opcao != 6:

    print(
        """ 
    [1] Somar
    [2] Multiplicar
    [3] Dividir
    [4] Maior
    [5] Menor
    [6] Sair do programa
    """
    )

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"A soma de {num1} + {num2} é igual a {num1 + num2}.")

    elif opcao == 2:
        print(f"A multiplicação entre {num1} e {num2} é igual a {num1 * num2}.")

    elif opcao == 3:
        if num2 != 0:
            print(f"A divisão entre {num1} e {num2} é igual a {num1 / num2:.2f}.")
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif opcao == 4:
        maior = num1 if num1 > num2 else num2
        print(f"O maior número entre {num1} e {num2} é {maior}.")

    elif opcao == 5:
        menor = num1 if num1 < num2 else num2
        print(f"O menor número entre {num1} e {num2} é {menor}.")

    elif opcao == 6:
        print("Saindo do programa...")
        print("Até mais!")

    else:
        print("Opção inválida. Tente novamente.")
    print("-=" * 15)
    sleep(2)
