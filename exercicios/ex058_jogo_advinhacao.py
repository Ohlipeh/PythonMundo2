# Exercício 058: Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computer = randint(0, 10)  # Faz o comoputador "pensar"
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)

acertou = False
palpite = 0

while not acertou:
    player = int(input("Em que número eu pensei? "))  # Jogador tenta adivinhar
    palpite += 1

    if player == computer:
        acertou = True
    elif player < computer:
        print("Mais... Tente novamente.")
    elif player > computer:
        print("Menos... Tente novamente.")

print(f"Acertou com {palpite} tentativas! Parabéns!.")
