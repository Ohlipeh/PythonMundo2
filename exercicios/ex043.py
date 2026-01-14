print("\033[1;32m" + "-=-" * 20 + "\033[m")

print("Cálculo do Índice de Massa Corporal (IMC)")

print("\033[1;32m" + "-=-" * 20 + "\033[m")

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura**2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")

elif 18.5 <= imc < 25:
    print("Você está no peso ideal.")

elif 25 <= imc < 30:
    print("Você está com sobrepeso.")

elif 30 <= imc < 40:
    print("Você está com obesidade.")

else:
    print("Você está com obesidade mórbida.")
