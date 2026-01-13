nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média foi {media:.1f}")
if media < 5.0:
    print("Você está REPROVADO.")
elif 5.0 <= media < 6.9:
    print("Você está de RECUPERAÇÃO.")
else:
    print("Você está APROVADO.")
print("Fim do programa.")
