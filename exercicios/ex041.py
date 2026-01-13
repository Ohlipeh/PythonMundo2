# Classificação de atletas por idade
import datetime

# Pega o ano atual
ano_atual = datetime.date.today().year
nasc = int(input("Ano de nascimento: "))
idade = ano_atual - nasc

# Classificação por idade
if idade <= 9:
    print(f"Você tem {idade} anos.")
    print("Categoria: MIRIM")

elif idade <= 14:
    print(f"Você tem {idade} anos.")
    print("Categoria: INFANTIL")

elif idade <= 19:
    print(f"Você tem {idade} anos.")
    print("Categoria: JÚNIOR")

elif idade <= 25:
    print(f"Você tem {idade} anos.")
    print("Categoria: SÊNIOR")

else:
    print(f"Você tem {idade} anos.")
    print("Categoria: MASTER")
