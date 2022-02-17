hourValue = float(input("Digite o valor da hora trabalhada: "))
quantityValue = int(input("Digite a quantidade de horas trabalhadas no mês: "))

total = hourValue * quantityValue
inss = total * 0.1
fgts = total * 0.11

if (total <= 900.00):
    print ("Isento de impostos.")

elif (total > 900.00 and total <= 1500.00):
    ir = total * 0.05
    descontos = ir + inss
    salarioLiquido = total - descontos
    print (f'Salário Bruto: ({hourValue:.0f} * {quantityValue:.0f}) - R$ {total:.2f} \n(-) IR (5%) - R$ {ir:.2f} \n(-) INSS (10%) - R$ {inss:.2f} \nFGTS (11%) - R$ {fgts:.2f} \nTotal de descontos - R$ {descontos:.2f} \nSalário Líquido - R$ {salarioLiquido:.2f}')

elif (total > 1500.00 and total <= 2500.00):
    ir = total * 0.1
    descontos = ir + inss
    salarioLiquido = total - descontos
    print (f'Salário Bruto: ({hourValue:.0f} * {quantityValue:.0f}) - R$ {total:.2f} \n(-) IR (10%) - R$ {ir:.2f} \n(-) INSS (10%) - R$ {inss:.2f} \nFGTS (11%) - R$ {fgts:.2f} \nTotal de descontos - R$ {descontos:.2f} \nSalário Líquido - R$ {salarioLiquido:.2f}')

elif (total > 2500.00):
    ir = total * 0.2
    descontos = ir + inss
    salarioLiquido = total - descontos
    print (f'Salário Bruto: ({hourValue:.0f} * {quantityValue:.0f}) - R$ {total:.2f} \n(-) IR (20%) - R$ {ir:.2f} \n(-) INSS (10%) - R$ {inss:.2f} \nFGTS (11%) - R$ {fgts:.2f} \nTotal de descontos - R$ {descontos:.2f} \nSalário Líquido - R$ {salarioLiquido:.2f}')   