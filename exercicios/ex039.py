import datetime

# Pega o ano atual
ano_atual = datetime.date.today().year

while True:
    print("\033[0;40m" + "-" * 30 + "\033[m")
    print("\033[0;42m SISTEMA DE ALISTAMENTO MILITAR \033[m")
    print("\033[0;40m" + "-" * 30 + "\033[m")

    # --- Validação do ano (sub-loop) ---
    while True:
        try:
            nasc = int(input(f"Que ano você nasceu? "))
            # Validação simples de coerência
            if nasc > ano_atual or nasc < ano_atual - 120:
                print(f"\033[0;31mERRO: Ano inválido. Tente novamente.\033[m")
                continue
            break
        except ValueError:
            print(f"\033[0;31mERRO: Entrada inválida. Digite um ano válido.\033[m")

    # --- Calculos ---
    idade = ano_atual - nasc
    print(f"Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.")

    sexo = input("Qual seu sexo? [M/F] ").strip().upper()

    # --- Lógica de alistamento ---
    if sexo == "F":
        print("O alistamento militar NÃO é obrigatório para mulheres.")

    elif sexo == "M":
        print("O alistamento militar é obrigatório para homens.")

        # A verificação de idade fica dentro do masculino
        if idade < 18:
            saldo = 18 - idade
            ano_alistamento = ano_atual + saldo
            print(f"Ainda faltam {saldo} anos para o alistamento.")
            print(f"Seu alistamento será em {ano_alistamento}.")

        elif idade == 18:
            print("Se você tem 18 anos. Você deve se alistar IMEDIATAMENTE!")

        else:  # Maior que 18
            saldo = idade - 18
            ano_alistamento = ano_atual - saldo
            print(f"Você já deveria ter se alistado há {saldo} anos.")
            print(f"Seu alistamento foi em {ano_alistamento}.")

    else:
        print(f"\033[0;31mERRO: Sexo inválido. Por favor, responda com M ou F.\033[m")

    # --- Pergunta para continuar ---
    resp = input("\nQuer verificar outra pessoa? [S/N] ").strip().upper()
    if resp == "N":
        print("Encerrando o sistema de alistamento militar. Até mais!")
        break
