#5


nome = str(input("digite o nome do aluno: "))


notaUm = float(input("digite a primeira nota do aluno: "))
notaDois = float(input("digite a segunda nota do aluno: "))


media = (notaUm + notaDois) / 2


media = str(media)


print("O aluno cujo nome: " + nome + ", obteve a seguinte nota de média: " + media + " onde se encontra situação: ")


media = float(media)


if media >= 7 and media <=10:
    print("Aprovado!")
   
elif media <= 7 and media >= 5:
    print("Recuperação.")
   
else:
    print("Reprovado!")