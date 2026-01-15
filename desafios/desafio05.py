# for i in range(1, 11):
#     print(f"Tabuada do {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Linha em branco para separar as tabuadas

# n = int(input("Digite um valor: "))
# for c in range(0, n + 1):
#     print(c)
# print("FIM")

# i = int(input("Início: "))
# m = int(input("Meio: "))
# f = int(input("Fim: "))
# for c in range(i, m + 1, f):
#     print(c)
# print("FIM")

s = 0
for i in range(0, 3):
    n = int(input("Digite um valor: "))
    s += n
print(f"A soma dos valores é {s}")
