# Exercício 066: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag).

soma = cont = 0
while True:
    numero = int(input("Digite um número (ou -1 para sair): "))
    if numero == -1:
        break
    soma += numero
    cont += 1
print(f"A quantidade de números digitados é: {cont} e a soma é: {soma}")
