num = int(input("Digite um número: "))
count = 0
for c in range(1, num + 1):
    if num % c == 0:
        print (f'\033[33m', end='')
        count += 1
    else:
        print (f'\033[31m', end='')

    print (f'{c} ', end='')

print (f'\n\033[mO número {num} foi divisível {count} vezes.')
if count == 2:
    print ("Número PRIMO!")
else:
    print ("Não é PRIMO!")