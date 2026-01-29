total = totmil = menor = maior = cont = 0
barato = " "
caro = " "

while True:

    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
        maior = preco
        caro = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

        if preco > maior:
            maior = preco
            caro = produto

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]? ")).strip().upper()
    if resp == "N":
        break

print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"O total da compra foi {total:.2f}.")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}.")
print(f"O produto mais caro foi {caro} que custa R${maior:.2f}.")
