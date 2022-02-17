nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if (media >= 9.0 and media <= 10.0):
    print("Conceito A, Aprovado(a)!")
elif (media >= 7.5 and media < 9.0):
    print("Conceito B, Aprovado(a)!")
elif (media >= 6.0 and media < 7.5):
    print("Conceito C, Aprovado(a)!")
elif (media >= 4.0 and media < 6.0):
    print ("Conceito D, Reprovado(a)!")
elif (media >= 0.0 and media < 4.0):
    print ("Conceito E, Reprovado(a)!")