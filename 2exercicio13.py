#13


aco = int(input("digite quantos hastes de aço foram compradas:"))
cobre = int(input("digite quantos hastes de cobre foram compradas:"))
aluminio = int(input("digite quantos hastes de alumínio foram compradas:"))

fe = aco * 2.50
cu = cobre * 4
al = aluminio * 5

soma = aco + cobre + aluminio
compra = fe + cu + al

desconto1 = compra 
desconto2 = compra - ( 10 / 100 )
desconto3 = compra - ( 15 / 100 )
desconto4 = compra - (20 / 100 ) 

if soma < 6:
    print("R$ " + str(desconto1) + " reais")
    
elif soma > 7 and soma < 15:
    print("R$ " + str(desconto2) + " reais")
    
elif soma > 16 and soma < 20:
    print("R$ " + str(desconto3) + " reais")
    
if soma > 20:
    print("R$ " + str(desconto4) + " reais")
