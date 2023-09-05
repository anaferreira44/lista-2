#12

sexo = str(input("digite seu sexo: "))
idade = int(input("digite sua idade (em anos):"))

if sexo == homem:
    if idade <= 20:
        print("jovem")
    
    elif idade >= 21:
        print("adulto")
    
elif sexo == mulher:
    if idade <= 17:
        print("jovem")
    
    elif idade >= 18:
        print("adulta")
