#16

num = int(input("Digite um numero de três digitos: "))

if 100 <= num <= 999:
    
    numCentena = num // 100
    numDezena = num % 100
    numDezena = numDezena // 10
    numUnidade = num % 10
    
    somaNum = numCentena + numDezena + numUnidade
    
    print("A soma de cada digito é igual a: " +str(somaNum))
    
    if somaNum % 16 == 0 and somaNum % 4 == 0:
        print("A soma dos digitos é divisivel por 16 e multiplo de 4")
    
    else:
        print("A soma dos digitos não é divisivel por 16 e multiplo de 4")
    
elif num <= 99 or num >=1000:
        print("tente novamente!")
    
else:
    print("O dado não esta válido")

