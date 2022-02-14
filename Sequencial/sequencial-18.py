arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidadeLink = int(input("Digite a velocidade da Internet em Mbps: "))

seg = arquivo / (velocidadeLink/8)
if (seg < 60):
    print (f'Tempo de Download em Segundos: {seg:.2f}')
else:
    min = seg / 60 
    print (f'Tempo em minutos do Download {min:.2f}')