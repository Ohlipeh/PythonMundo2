# Iniciando o loop principal
while True:
    print("-=" * 20)  # Separador visual
    try:  # Captura de entrada do usuário
        # Se o usuário não digitar nada ou texto, o programa não quebra
        entrada = input("Digite um número inteiro (ou '999' para parar): ")
        if entrada == "999":
            break
        num = int(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue  # Reinicia o loop se a entrada for inválida

    print("Escolha a base para conversão:")
    print("[ 1 ] converter para BINÁRIO")
    print("[ 2 ] converter para OCTAL")
    print("[ 3 ] converter para HEXADECIMAL")

    opção = int(input("Sua opção: "))

    if opção == 1:
        print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
    elif opção == 2:
        print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
    elif opção == 3:
        print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
    else:
        print("Opção inválida!")

    # Pergunta se o usuário deseja continuar
    continuar = input("\nDeseja continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break  # O comando 'break' encerra o loop principal

print("Programa encerrado. Obrigado por usar o conversor!")
