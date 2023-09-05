#3

ano = int(input("Digite o ano atual: "))

nome1 = input("digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

if idade1 > idade2:
    print(nome2 +" é mais novo(a) que " + nome1 + "e nasceu em " + (ano - idade2))
    
elif idade1 == idade2:
    print(nome1 + " e " + nome2 + " tem a mesma idade e nasceram em " + (ano - idade1))
    
else:
    print(nome1 + " é mais novo(a) e nasceu em " + str(ano - idade1))
