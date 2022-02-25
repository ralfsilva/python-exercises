numero = 326
centena_str = dezena_str = unidade_str = ''
centena_int, numero = divmod(numero, 100)

if centena_int == 1:
    centena_str = '1 centena'
elif centena_int > 1:
    centena_str = f'{centena_int} centenas' 

dezena_int, numero = divmod(numero, 10)

if dezena_int == 1:
    dezena_str = '1 dezena'
elif dezena_int > 1:
    dezena_str = f'{dezena_int} dezenas'

if numero == 1:
    unidade_str = '1 unidade'
elif numero > 1:
    unidade_str = f'{numero} unidades'

print (centena_str, dezena_str, unidade_str)