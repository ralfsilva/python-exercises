respondeIdade = 's'
total = 0
jovem = 0
adulta = 0
idosa = 0

while respondeIdade == 's':
    idade = int(input("Digite a sua idade: "))
    total += 1

    if idade >= 0 and idade <= 25:
        jovem += 1
    elif idade > 25 and idade <= 60:
        adulta += 1
    elif idade > 60:
        idosa += 1
    
    mediaJovem = jovem / total * 100
    mediaAdulta = adulta / total * 100
    mediaIdosa = idosa / total * 100
    
    print (f'A população é dividida em: \nJovem -> {mediaJovem:.2f} % \nAdulta -> {mediaAdulta:.2f} % \nIdosa -> {mediaIdosa:.2f} %')