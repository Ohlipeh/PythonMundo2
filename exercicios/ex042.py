# Analisador de Triângulos
print("\033[0;31;101m" "-=" * 20 + "\033[m")

print("ANALISADOR DE TRIÂNGULOS")

print("\033[0;31;101m" "-=" * 20 + "\033[m")

# Entrada dos segmentos
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

# Verificação se podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo", end=" ")
    # Condição aninhada
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:  # (!) significa que são todos diferentes
        print("ESCALENO!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
