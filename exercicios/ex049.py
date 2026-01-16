tabuada = int(input("Digite um número para ver sua tabuada: "))
print("-" * 12)
for c in range(1, 11):
    print(f"{tabuada} x {c:2} = {tabuada * c}")
