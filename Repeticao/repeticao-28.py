totalCd = 0
count = 0
contaCd = 1

colecao = int(input("Qual o número de CD's da coleção: "))

while count < colecao:
    valorCd = float(input(f'Digite o valor pago pelo CD {contaCd}: '))
    totalCd += valorCd

    mediaColecao = totalCd / colecao

    count += 1
    contaCd += 1

print (f'O valor pago em toda a coleção foi R$ {totalCd:.2f} e a média em cada CD foi de R$ {mediaColecao:.2f}')