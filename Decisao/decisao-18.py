dia = int(input("Digite o dia para uma determinada Data: "))
mes = int(input("Digite o mês para uma determinada Data: "))
ano = int(input("Digite o ano para uma determinada Data: "))

if (mes <= 12):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if (dia <= 31):
            print ("A sua Data {}/{}/{} está correta.".format(dia,mes,ano))
        else:
            print("Data inválida.")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30):
            print ("A sua Data {}/{}/{} está correta.".format(dia,mes,ano))
        else:
            print("Data inválida.")
    elif (mes == 2):
        if (dia <= 28 or dia <= 29 and ano % 4 == 0):
            print ("A sua Data {}/{}/{} está correta.".format(dia,mes,ano))
        elif ():
            print ("A sua Data {}/{}/{} está correta.".format(dia,mes,ano))
        else:
            print("Data inválida.")
else:
    print("Data inválida.")