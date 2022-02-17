lado1 = float(input("Informe o valor do primeiro lado para o triângulo: "))
lado2 = float(input("Informe o valor do segundo lado para o triângulo: "))
lado3 = float(input("Informe o valor do terceiro lado para o triângulo: "))

lado12 = lado1 + lado2
lado13 = lado1 + lado3
lado23 = lado2 + lado3

if (lado12 > lado3 or lado13 > lado2 or lado23 > lado1):
    if (lado1 == lado2 == lado3):
        print ("Triângulo Equilátero.")
    elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
        print ("Triângulo Isósceles.")
    elif (lado1 != lado2 != lado3):
        print ("Triângulo Escaleno.")

else:
    print ("Essas medidas não geram um triângulo.")