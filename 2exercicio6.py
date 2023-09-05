#6

media = float(input("digite a média do aluno: "))
faltas = int(input("digite o numero de faltas do aluno: "))

if media >= 7 and faltas<= 32:
    print("Aprovado!")
    
elif media <= 7 and faltas<= 32:
    print("Reprovado por Média!")
    
elif media >= 7 and faltas >= 32:
    print("Reprovado por Faltas!")
    
else:
    print("Reprovado por por Média e Faltas!")

