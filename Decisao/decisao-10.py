turno = input("Informe o turno que você estuda, digite M, V ou N: ")

if (turno == 'm' or turno == 'M'):
    print ("Matutino!")
elif (turno == 'v' or turno == 'V'):
    print ("Vespertino!")
elif (turno == 'n' or turno == 'N'):
    print ("Noturno!")
else:
    print("Inválido.")