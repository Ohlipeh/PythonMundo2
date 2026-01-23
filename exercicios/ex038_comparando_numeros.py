## Exercício 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
# uma mensagem:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print("O \033[0;31m PRIMEIRO \033[m número é maior.")
elif num2 > num1:
    print("O \033[1;34m SEGUNDO \033[m número é maior.")
else:
    print("Os dois números são iguais.")
