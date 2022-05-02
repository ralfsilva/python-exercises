eleitor = 0
voto = 0
fulano = 0
ciclano = 0
beltrano = 0
count = 0

eleitor = int(input("Digite o número de eleitores: "))

while count < eleitor:
    count += 1

    candidato = int(input("Os candidatos são: Fulano (1) - Ciclano (2) - Beltrano (3)\n"))
    voto += 1

    if candidato == 1:
        fulano += 1
    elif candidato == 2:
        ciclano += 1
    elif candidato == 3:
        beltrano += 1
    else:
        print ("Voto Incorreto!")

    votoFulano = fulano / voto * 100
    votoCiclano = ciclano / voto * 100
    votoBeltrano = beltrano / voto * 100

print (f'\nTotal de votos: Fulano -> {votoFulano:.2f} % - Ciclano -> {votoCiclano:.2f} % - Beltrano -> {votoBeltrano:.2f} %')