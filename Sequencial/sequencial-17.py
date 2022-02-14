metro = float(input("Informe o tamanho em metros quadrados a serem pintados: "))
coberturaLatas = metro/6
coberturaGalon = metro/6
coberturaMistura = metro/6

precoLatas = 1
precoGalon = 1
precoMisturaLata = 0
precoMisturaGalon = 0

# Cálculo para as Latas de tinta
while (coberturaLatas >= 18.0):
    coberturaLatas -= 18.0
    precoLatas += 1

# Cálculo para os galões de tinta
while (coberturaGalon >= 3.6):
    coberturaGalon -= 3.6
    precoGalon += 1

# Cálculo para a mistura
coberturaMistura = coberturaMistura + (coberturaMistura * 0.10)
while (coberturaMistura >= 18.0):
    coberturaMistura -= 18.0
    precoMisturaLata += 1
    if (coberturaMistura >= 3.6):
        coberturaMistura -= 3.6
        precoMisturaGalon += 1

precoLatas *= 80
precoGalon *= 25
precoMisturaLata *= 80
precoMisturaGalon *= 25
precoMistura = precoMisturaLata + precoMisturaGalon

print("O valor das latas é de: R$ {}".format(precoLatas))
print("O valor dos Galões é de: R$ {}".format(precoGalon))
print("O Valor da mistura entre galões e latas: R$ {}".format(precoMistura))