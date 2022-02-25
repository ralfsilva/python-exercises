nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print (f'Aprovado - Nota: {media}')
elif media < 7.0:
    print (f'Reprovado - Nota: {media}')
elif media == 10.0:
    print (f'Aprovado com Distinção - Nota: {media}')