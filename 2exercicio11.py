#11

ano = int(input("Digite o ano: "))
mes = str(input("Digite o mes: "))

janeiro = 31
fevereiro = 28
marco = 31
abril = 30
maio = 31
junho = 30
julho = 31
agosto = 31
setembro = 30
outubro = 31
novembro = 30
dezembro = 31

if mes == "janeiro":
    print("O mes de janeiro tem: " + str(janeiro) + " dias")

elif mes == "fevereiro":
    if ano % 4 == 0:
        if ano % 100 != 0 or ano % 400 == 0:
            fevereiro = 29
            
            print("O ano é bissexto, então o mes de fevereiro tem: "
            + str(fevereiro) + " dias")
        else:
            print("O ano não é bissexto, então o mes de fevereiro tem: " + str(fevereiro) + " dias")
    else:
        print("O ano não é bissexto, então o mes de fevereiro tem: " + str(fevereiro) + " dias")

elif mes == "marco":
    print("O mes de março tem: " + str(marco) + " dias")
    
elif mes == "abril":
    print("O mes de abril tem: " + str(abril) + " dias")

elif mes == "maio":
    print("O mes de maio tem: " + str(maio) + " dias")
    
elif mes == "junho":
    print("O mes de junho tem: " + str(junho) + " dias")

elif mes == "julho":
    print("O mes de julho tem: " + str(julho) + " dias")
    
elif mes == "agosto":
    print("O mes de agosto tem: " + str(agosto) + " dias")

elif mes == "setembro":
    print("O mes de setembro tem: " + str(setembro) + " dias")
    
elif mes == "outubro":
    print("O mes de outubro tem: " + str(outubro) + " dias")

elif mes == "novembro":
    print("O mes de novembro tem: " + str(novembro) + " dias")

elif mes == "dezembro":
    print("O mes de dezembro tem: " + str(dezembro) + " dias")
    

