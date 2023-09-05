#2

distanciaCarro1 = float(input("digite a distância (em km) que o primeiro carro percorreu: "))

distanciaCarro2 = float(input("digite a distância (em km) que o segundo carro percorreu: "))

tempoCarro1 = int(input("digite quanto tempo (em minutos) que o primeiro carro percorreu: " ))

tempoCarro2 = int(input("digite quanto tempo (em minutos) que o segundo carro percorreu: " ))

mediaCarro1 = distanciaCarro1 / tempoCarro1
mediaCarro2 = distanciaCarro2 / tempoCarro2

mediaCarro1 = float(mediaCarro1)
mediaCarro2 = float(mediaCarro2)

if (mediaCarro1 > mediaCarro2):
    print("o carro 1 teve uma velocidade media maior que o carro 2")
    
elif (mediaCarro1 == mediaCarro2):
    print("o carro 1 teve uma velocidade media igual que o carro 2")
    
else: 
    print("o carro 2 teve uma velocidade media maior que o carro 1")
