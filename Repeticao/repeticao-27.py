import math

count = 0
alunos = 0
contaTurma = 1
totalAlunos = 0

turma = int(input("Digite a quantidade de turmas: "))

while count < turma:
    alunos = int(input(f'Digite a quantidade de Alunos na Turma {contaTurma}: '))
    totalAlunos += alunos

    if alunos > 40:
        print ("As turmas não podem ter mais de 40 alunos.")
        totalAlunos -= alunos
        count -= 1
        contaTurma -= 1

    mediaAlunos = totalAlunos / turma

    count += 1
    contaTurma += 1

print (f'A média de alunos em cada turma é de {math.floor(mediaAlunos)}')