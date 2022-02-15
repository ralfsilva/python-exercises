def maisBarato(p1, p2 ,p3):
    barato = p1

    if (p2 < barato):
        barato = p2
    if (p3 < barato):
        barato = p3

    return barato

def produto():
    p1 = float(input("Digite o preço da Tv: "))
    p2 = float(input("Digita o preço do SmartPhone: "))
    p3 = float(input("Digite o preço do Nintendo Switch: "))
    
    print ("O produto mais barato é o: ", maisBarato(p1, p2, p3))

produto()