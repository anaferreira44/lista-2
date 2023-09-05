#15

hI = int(input("Digite a hora inicial: "))
minI = int(input("Digite o minuto inicial: "))

hFim = int(input("Digite a hora final: "))
minFim = int(input("Digite o minuto final: "))

if hI <= 23 and hFim <= 23:
    if minI <= 59 and minFim <= 59:
        minT = ((hFim * 60) + minFim) - ((hI * 60) + minI)
        
        hJ = minT // 60
        minT %= 60
        
        if hJ < 0:
            hJ = -1 * hJ
            hJ = 24 - hJ
            
        if mT == 0:
            print("Você jogou durante " + str(hJ) + " horas")
        
        else:
            print("Você jogou durante " + str(hJ) + " horas e " + str(minT) + " minutos")
    
    else:
        print("Entrada de dados não válida!")
    
else:
    print("Entrada de dados não válida!")
