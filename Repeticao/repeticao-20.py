fat = 1
total = 0

while fat > 0:
    fat = int(input("Digite o número para ser demonstrado o fatorial:  "))
    if fat < 16:
        total += fat * (fat - 1)
        print (f'Fatorial de {fat}: {fat}', end='')
        fat -= 1
        while fat > 1:
            print (f' x {fat}', end='')
            fat -= 1
            mult = total * fat
            total = mult
        
        print (f' x {fat} = {total}', end='')