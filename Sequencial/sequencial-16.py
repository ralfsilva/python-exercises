tinta = float(input("Qual o tamanho da área a ser pintada em metros quadrados?"))

cobertura = tinta/3
count = cobertura
preco = 1

while (count >= 18):
    preco += 1
    count -= 18
    
preco = preco * 80

print (f'Então vão ser gastos {cobertura:.2f} litro(s) de tinta e preço será de R$ {preco:.2f}.')
