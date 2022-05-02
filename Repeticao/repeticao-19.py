x = 0
tentativas = 5
maior = 0
menor = 9999

while x < 5:
    numero = int(input(f'Digite um Número, você possui {tentativas} tentativas: '))
    if numero > 0 and numero < 1000:

        if maior < numero:
            maior = numero
        if menor > numero:
            menor = numero

    else:
        print ("Digite um número entre 0 e 1000.")

    tentativas -= 1
    x += 1

soma = maior + menor

print (f'A soma dos valores {maior} e {menor} = {soma}')