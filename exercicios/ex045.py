from random import randint
from time import sleep

itens = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
computador = randint(0, 4)
print("Suas opções:")
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")
print("3 - Lagarto")
print("4 - Spock")

jogador = int(input("Escolha sua jogada (0-4): "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=" * 15)
print(f"Computador escolheu: {itens[computador]}")
print(f"Jogador escolheu: {itens[jogador]}")
print("-=" * 15)

regras_vitoria = {
    0: [2, 3],  # Pedra (0) ganha de: Tesoura (2) e Lagarto (3)
    1: [0, 4],  # Papel (1) ganha de: Pedra (0) e Spock (4)
    2: [1, 3],  # Tesoura (2) ganha de: Papel (1) e Lagarto (3)
    3: [4, 1],  # Lagarto (3) ganha de: Spock (4) e Papel (1)
    4: [2, 0],  # Spock (4) ganha de: Tesoura (2) e Pedra (0)
}

# Logica para determinar o vencedor
if jogador == computador:
    print("Empate!")

# 1. 'regras_vitoria[computador]' acessa a LISTA de quem o PC vence.
#    Ex: Se PC jogou Pedra (0), isso retorna a lista [2, 3].
# 2. O operador 'in' verifica: "A jogada do jogador está DENTRO dessa lista?"
elif jogador in regras_vitoria[computador]:
    print("Computador venceu!")

# Se não empatou e o jogador não está na lista de "vítimas" do PC,
# então o jogador ganhou.
else:
    print("Jogador venceu!")
