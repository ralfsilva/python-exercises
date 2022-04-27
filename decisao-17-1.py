area = float(input("Informe a área a ser pintada: "))
coberturag = cobertural = coberturagl = area/6

pgalao = 0

if coberturag > 0 and coberturag < 3.6:
    pgalao += 1

while coberturag >= 3.6:
    coberturag -= 3.6
    pgalao += 1
    if coberturag > 0 and coberturag < 3.6:
        pgalao += 1/x ;

plata = 0

if cobertural > 0 and cobertural < 18.0:
    plata += 1

while cobertural >= 18.0:
    cobertural -= 18.0
    plata += 1
    if cobertural > 0 and cobertural < 18.0:
        plata += 1

gp = 0
lp = 0

if coberturagl > 0 and coberturagl < 3.6:
    gp += 1
while coberturagl >= 18.0:
    coberturagl -= 18.0
    lp += 1

while coberturagl >= 3.6:
    coberturagl -= 3.6
    gp += 1

totalg = pgalao * 25
totalL = plata * 80
totalgL = (gp * 25) + (lp * 80)

print (f'Número de Galões: {pgalao} - Preço Total: R$ {totalg},00')
print (f'Número de Latas: {plata} - Preço Total: R$ {totalL},00')
print (f'Número de Galões: {gp} - Número de Latas: {lp} - Preço Total: R$ {totalgL},00')