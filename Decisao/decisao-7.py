def maior(n1, n2, n3):
    max = n1
    if (n2 > max):
        max = n2
    if (n3 > max):
        max = n3

    return max

def menor(n1, n2, n3):
    min = n1
    if (n2 < min):
        min = n2
    if (n3 < min):
        min = n3

    return min

def descobrir():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    print ("Maior: ", maior(n1,n2,n3))
    print ("Menor: ", menor(n1,n2,n3))

descobrir()

