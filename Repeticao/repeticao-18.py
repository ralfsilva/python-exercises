x = 0
maior = 0
menor = 9999

while x < 5:
    numero = int(input("Digite um Número: "))

    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero

    x += 1

soma = maior + menor

print (f'A soma dos valores {maior} e {menor} = {soma}')