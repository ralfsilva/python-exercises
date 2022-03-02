morango = int(input("Digite quantos KG de Morango vai comprar: "))
maca = int(input("Digite quantos KG de Maçã vai comprar: "))

frutas = morango + maca
valor = 0
verdade = True

while verdade:
    if morango <= 5:
        valor += float(morango * 2.50)
    if morango > 5 and morango <= 11:
        valor += float(morango * 2.20)
    if maca <= 5:
        valor += float(maca * 1.80)
    if maca > 5 and morango <= 16:
        valor += float(maca * 1.50)
    if frutas > 8 or valor >= 25.00:
        valor = valor - (valor * 0.1)
    verdade = False

print (f'O valor total: R$ {valor:.2f}')