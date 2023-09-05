#10

salario = float(input("digite o valor do seu salário bruto: "))
print("salario bruto é: " + str(salario)) 

imposto1 = salario * 0.075 
imposto2 = salario * 0.15 
imposto3 = salario * 0.225 
imposto4 = salario * 0.275 

d1 = imposto1 - salario
d2 = imposto2 - salario
d3 = imposto3 - salario
d4 = imposto4 - salario

if salario <= 1903.98:
    print("isento")
    
elif salario >= 1903.99 and salario <= 2826.65:
    print("o valor de imposto de renda pago será: " + str(imposto1))
    
elif salario >= 2826.66 and salario <= 3751.05: 
    print("o valor de imposto de renda pago será: " + str(imposto2))
    
elif salario >= 3751.06 and salario <= 4664.68: 
    print("o valor de imposto de renda pago será: " + str(imposto3))
    
elif salario >= 4664.69: 
    print("o valor de imposto de renda pago será: " + str(imposto4))
