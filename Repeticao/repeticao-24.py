nota = 0
total = 0
count = 0
adicionar = 's'

while adicionar == 's':
    nota = float(input("Digite uma nota: "))
    total += nota
    count += 1
    media = total / count

    adicionar = input("Deseja adicionar mais alguma nota? (s)im ou (n)ão")

print (f'Foram adicionadas {count} notas, com um resultado de {total} e uma média de {media}')