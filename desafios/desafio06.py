## Exemplo de laços de repetição em Python

# for c in range(1, 11):
#   print(c, end=' ')
# print('FIM')

# c = 1
# while c <= 10:
#     print(c, end=" ")
#     c += 1
# print("FIM")

# r = "S"
# while r == "S":
#     n = int(input("Digite um valor: "))
#     r = str(input("Quer continuar? [S/N] ")).upper()
# print("FIM")

# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input("Digite um valor (0 para parar): "))
#     if n != 0:
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# print(f"Você digitou {par} números pares e {impar} números ímpares.")

# contador = 10

# while contador >= 1:
#     print(contador)
#     contador -= 1

# print("Fogo!!!")

# senha_correta = 1234
# senha_digitada = ""

# while senha_digitada != senha_correta:
#     senha_digitada = int(input("Digite a senha: "))

# print("Acesso permitido.")

soma = 0
numero = 1

while soma < 20:
    soma += numero
    print(f"A somamdo {numero}... Total agora é {soma}")
    numero += 1
print("Acabou!")