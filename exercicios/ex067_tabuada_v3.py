# Tabuada v3.0 - Repetição com condição de parada
# Exercício 067: Melhore o exercício 66, mostrando no final a tabuada de todos os números
# digitados, incluindo o 999 que encerra o programa.

while True:
    num = int(
        input("Digite um número para ver a tabuada (ou um número negativo para sair): ")
    )
    if num < 0:
        print("Programa encerrado.")
        break
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)
print("Obrigado por usar o programa de tabuada!")
