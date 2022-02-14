workedHour = float(input("Digite o quanto ganha por hora: "))
valueHour = int(input("Digite o número de horas traballhadas: "))

salary = workedHour * valueHour

ir = (salary * 11/100)
inss = (salary * 8/100)
sindicato = (salary * 5/100)
liquidSalary = salary - ir - inss - sindicato

print (f'Salário Bruto: R$ {salary:.2f} \nValor pago de IR: R$ {ir:.2f} \nValor pago de INSS: R$ {inss:.2f} \nValor pago ao sindicato: R$ {sindicato:.2f} \nSalário Líquido: R$ {liquidSalary:.2f}')
