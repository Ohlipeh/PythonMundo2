# Análise de dados de um grupo de 4 pessoas

print("ANÁLISE DE DADOS DE UM GRUPO DE 4 PESSOAS")

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_maior_idade = ""
total_mulheres_menos_20 = 0

for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    soma_idade += idade
    if p == 1 and sexo == "M":
        maior_idade_homem = idade
        nome_maior_idade = nome

    if sexo == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_maior_idade = nome

    if sexo == "F" and idade < 20:
        total_mulheres_menos_20 += 1

media_idade = soma_idade / 4

print("----- RESULTADOS -----")
print(f"A média de idade do grupo é de {media_idade} anos.")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_maior_idade}.")
print(f"Ao todo são {total_mulheres_menos_20} mulheres com menos de 20 anos.")
