salario = float(input("Digite o Salário do Colaborador: "))

print ("Salário antes do reajuste: R$",salario)

if (salario <= 280.00):
    vintePorCento = 0.2
    percent = salario * vintePorCento
    reajuste = salario + percent
    print (f'O salário aumentou em: {vintePorCento:.2f}%')
    print (f'O valor do aumento no salário: R$ {percent:.2f}')
    print (f'O valor com reajuste: R$ {reajuste:.2f}')

elif (salario > 280.00 and salario <= 700.00):
    quinzePorCento = 0.15
    percent = salario * quinzePorCento
    reajuste = salario + percent
    print (f'O salário aumentou em: {quinzePorCento:.2f}%')
    print (f'O valor do aumento no salário: R$ {percent:.2f}')
    print (f'O valor com reajuste: R$ {reajuste:.2f}')

elif (salario > 700.00 and salario <= 1500.00):
    dezPorCento = 0.10
    percent = salario * dezPorCento
    reajuste = salario + percent
    print (f'O salário aumentou em: {dezPorCento:.2f}%')
    print (f'O valor do aumento no salário: R$ {percent:.2f}')
    print (f'O valor com reajuste: R$ {reajuste:.2f}')

elif (salario > 1500.00):
    cincoPorCento = 0.05
    percent = salario * cincoPorCento
    reajuste = salario + percent 
    print (f'O salário aumentou em: {cincoPorCento:.2f}%')
    print (f'O valor do aumento no salário: R$ {percent:.2f}')
    print (f'O valor com reajuste: R$ {reajuste:.2f}')