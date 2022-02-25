saque = int(input("De quanto será o saque: "))
copy = saque

um = cinco = dez = cinq = cem = 0

if saque >= 10 and saque <= 600:
    while saque >= 100:
        saque -= 100
        cem += 1

    while saque >= 50 and saque < 100:
        saque -= 50
        cinq += 1

    while saque >= 10 and saque < 50:
        saque -= 10
        dez += 1
    
    while saque >= 5 and saque < 10:
        saque -= 5
        cinco += 1

    while saque >= 1 and saque < 5:
        saque -= 1
        um += 1
else:
    print ("Valor para saque inválido, tente novamente.")

print (f'Para sacar a quantia de {copy} reais, o programa fornece {cem} nota(s) de 100, {cinq} nota(s) de 50, {dez} nota(s) de 10, {cinco} nota(s) de 5 e {um} nota(s) de um.')