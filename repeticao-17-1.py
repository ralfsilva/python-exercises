res = 1

fat = int(input("Digite o número para ser mostrado o Fatorial: "))

for n in range(1, fat+1):
    res *= n
    
print (res)