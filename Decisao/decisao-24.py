num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

num3 = (num1 + num2)/2

operacao = input("O que você deseja fazer com os números? \na. Par ou impar \nb. Positivo ou negativo \nc. Inteiro ou decimal")

if operacao == 'a' or operacao == 'A':
    if num3 % 2 == 0:
        print ("O número {} é par.".format(num3))
    elif num3 % 2 != 0:
        print ("O número {} é impar.".format(num3))
elif operacao == 'b' or operacao == 'B':
    if num3 >= 0:
        print ("O número {} é positivo.".format(num3))
    else:
        print ("O número {} é negativo.".format(num3))
elif operacao == 'c' or operacao == 'C':
    if num3 == round(num3):
        print ("O número {} é inteiro.".format(num3))
    else:
        print ("O número {} é decimal.".format(num3))
else:
    print ("Escolha Inválida.")