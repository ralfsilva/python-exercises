numero = float(input("Informe um número: "))

if numero == round(numero):
    print ("inteiro.")
else:
    print ("Decimal.")
    print ("Arredondando para cima: ", round(numero+0.5))
    print ("Arredondando para baixo: ", round(numero-0.5))