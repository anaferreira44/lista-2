#9 

sexo = int(input("digite seu sexo (1-homem ou 2-mulher):"))
peso = float(input("digite o seu peso (em kg):"))
altura = float(input("digite sua altura (em centímetros):"))
idade = float(input("digite sua idade (em anos):"))

masc = 66 + ( 13.7 * peso ) + ( 5 * altura ) - ( 6.8 * idade )
femin = 665 + ( 9.6 * peso ) + ( 1.8 * altura ) - ( 4.7 * idade )

if sexo == 1:
    print(masc)

elif sexo == 2:
    print(femin)
    
else:
    print("faça novamente!")
