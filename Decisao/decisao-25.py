print ("Responda o questionário investigativo sobre o Crime: \n")

count = 0

q1 = int(input("Telefonou para a vítima? \n1 - Sim  -  2 - Não "))
q2 = int(input("Esteve no local do Crime? \n1 - Sim  -  2 - Não "))
q3 = int(input("Mora perto da vítima? \n1 - Sim  -  2 - Não "))
q4 = int(input("Devia para a vítima? \n1 - Sim  -  2 - Não "))
q5 = int(input("Telefonou para a vítima? \n1 - Sim  -  2 - Não "))

perg = [q1, q2, q3, q4, q5]

pergunta = True

while pergunta:
    if q1 == 1:
        count += 1
    if q2 == 1:
        count += 1
    if q3 == 1:
        count += 1
    if q4 == 1:
        count += 1
    if q5 == 1:
        count += 1
    pergunta = False

if count == 1:
    print ("A pessoa é Inocente.")
elif count == 2:
    print ("Esta pessoa é suspeita.")
elif count == 3 or 4:
    print ("Esta pessoa é Cúmplice.")
elif count == 5:
    print ("Esta pessoa é o Assassino!")