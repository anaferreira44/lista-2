#8

distancia = float(input("digite a distancia percorrida em kilometros: "))
combustivel = float(input("digite a quantidade combustivel que foi gasto em litros: "))

media = distancia / combustivel

if media <= 8:
    print("Venda o Carro!")
   
elif media >= 8 and media <= 14:
    print("Econômico!")
   
else:
    print("Super Econômico!")