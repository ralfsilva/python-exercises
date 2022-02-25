number = int(input("Digite um valor inteiro menor do que 1000: \n"))

copy = number
centena = 0
dezena = 0
unidade = 0

while (number >= 100):
    centena += 1
    number -= 100

while (number >= 10):
    dezena += 1
    number -= 10

while (number >= 1):
    unidade += 1
    number -= 1

if (centena > 1):
    print (f'{copy} = {centena} centenas, {dezena}')
elif (centena == 1):
    print ("{} = {} centena, {} dezenas e {} unidades.".format(copy, centena, dezena, unidade))
elif (dezena > 1):
    print ("{} = {} dezenas e {} unidades".format(copy, dezena, unidade))
elif (dezena == 1):
    print ("{} = {} dezena e {} unidades".format(copy, dezena, unidade))
elif (unidade > 1):
    print ("{} = {} unidades.".format(copy, unidade))
elif (unidade == 1):
    print ("{} = {} unidade.".format(copy, unidade))