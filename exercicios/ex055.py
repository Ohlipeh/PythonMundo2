# Exercício 055: Maior e Menor da Sequência
# Desenvolva um programa que leia o peso de sete pessoas. No final, mostre qual foi o maior
# e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa (kg): "))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f"O maior peso registrado foi de {maior_peso} kg.")
print(f"O menor peso registrado foi de {menor_peso} kg.")
