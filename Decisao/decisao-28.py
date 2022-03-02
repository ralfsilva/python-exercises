type = int(input("Escolha qual tipo de Carne você deseja digitando o número correspondente: \nFilé Duplo - 1 \nAlcatra - 2 \nPicanha - 3\n"))

valor = 0
verdade = True

if type == 1:
    quantity = int(input("Digite quantos KG de Filé Duplo vai querer: \n"))
    
    if quantity <= 5:
        valor = quantity * 4.90
    elif quantity > 5:
        valor = quantity * 5.80

elif type == 2:
    quantity = int(input("Digite quantos KG de Alcatra vai querer: \n"))
    
    if quantity <= 5:
        valor = quantity * 5.90
    elif quantity > 5:
        valor = quantity * 6.80

elif type == 3:
    quantity = int(input("Digite quantos KG de Alcatra vai querer: \n"))
    
    if quantity <= 5:
        valor = quantity * 6.90
    elif quantity > 5:
        valor = quantity * 7.80

tabajara = int(input("Vai usar o cartão tabajara? \nSim - 1 \nNão - 2\n"))
if tabajara == 1:
    valor = float(valor - (valor * 0.05))

print (f'O total ficou em: R$ {valor:.2f}')