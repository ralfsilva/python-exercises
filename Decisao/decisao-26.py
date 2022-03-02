litros = int(input("Digite a quantidade do combustível: "))
tipo = input("Especifique qual é o Combustível: \nA-álcool - G-gasolina -> ")

if tipo == 'A' or tipo == 'a':
    if litros <= 20:
        valor = float(litros * 1.90)
        total = float(valor - (valor * 0.03))
        print ("O valor a ser pago no álcool: R$ {}".format(total))
    elif litros > 20:
        valor = float(litros * 1.90)
        total = float(valor - (valor * 0.05))
        print ("O valor a ser pago no álcool: R$ {}".format(total))
elif tipo == 'G' or tipo == 'g':
    if litros <= 20:
        valor = float(litros * 2.50)
        total = float(valor - (valor * 0.04))
        print ("O valor a ser pago na gasolina: R$ {}".format(total))
    elif litros > 20:
        valor = float(litros * 2.50)
        total = float(valor - (valor * 0.06))
        print ("O valor a ser pago na gasolina: R$ {}".format(total))
else:
    print ("Escolha inválida! Tente novamente.")