numeroFatorial = int(input("Digite um número para ser demonstrado o fatorial: "))
fatorial = numeroFatorial
total = numeroFatorial * (numeroFatorial - 1)
numeroFatorial -= 1
print (f'Fatorial de {fatorial}: {fatorial} . {numeroFatorial}', end='')

while numeroFatorial > 1:
    numeroFatorial -= 1
    total = total * numeroFatorial
    print (f' . {numeroFatorial}', end='')
print (f' = {total}')    