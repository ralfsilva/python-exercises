def ImprimirN(): 
    x = 0
    n = int(input("Digite um numero wue irá pular linhas: "))

    while x < n:
        x += 1
        print (x * "{} ".format(x))

ImprimirN()