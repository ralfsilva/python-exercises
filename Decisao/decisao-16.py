import sys
import math

a = int(input("Digite o valor de A da equação: "))
if (a == 0):
    print ("A equação não é do segundo grau.")
    sys.exit()
b = int(input("Digite o valor de B da equação: "))
c = int(input("Digite o valor de C da equação: "))

delta = (b * b) - 4 * a * c

if (delta < 0):
    print ("O delta é negativo, não há raizes reais.")
    sys.exit()

raiz1 = (- b + math.sqrt(delta)) / (2 * a)
raiz2 = (- b - math.sqrt(delta)) / (2 * a)

if (delta == 0):
    print ("Delta = 0, Raiz real: ",raiz1, raiz2)
elif (delta > 0):
    print ("Delta > 0, Raiz 1: {} - Raiz 2: {}".format(raiz1, raiz2))