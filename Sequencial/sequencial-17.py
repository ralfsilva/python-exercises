metro = float(input("Informe o tamanho em metros quadrados a serem pintados: "))
cobertura = metro/6

latas = 0
galao = 0
misturaGalao = 0
misturaLata = 0

# Cálculo para as Latas de tinta
coberturaLatas = cobertura
while (coberturaLatas >= 18.0):
    coberturaLatas -= 18.0
    latas += 1

# Cálculo para os galões de tinta
coberturaGalao = cobertura
while (coberturaGalao >= 3.6): 
    coberturaGalao -= 3.6
    galao += 1

# Cálculo para a mistura
#   coberturaMistura = coberturaMistura + (coberturaMistura * 0.10)
coberturaMistura = cobertura
coberturaMistura += (coberturaMistura * 0.1)
while (coberturaMistura >= 0.1):
    if coberturaMistura <= 10.8:
        coberturaMistura -= 3.6
        misturaGalao += 1     

    elif coberturaMistura > 10.8:
        coberturaMistura -= 18.0
        misturaLata += 1

latas *= 80
galao *= 25
misturaLata *= 80
misturaGalao *= 25
precoMistura = misturaLata + misturaGalao

print(f'O valor das latas é de: R$ {latas}')
print(f'O valor dos Galões é de: R$ {galao}')
print(f'O Valor da mistura entre galões e latas: R$ {precoMistura}')