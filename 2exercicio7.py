#7

ang1 = int(input("Digite o primeiro ângulo: "))
ang2 = int(input("Digite o segundo ângulo: "))
ang3 = int(input("Digite o terceiro ângulo: "))

if ang1 < 90 and ang2 < 90 and ang3 < 90:
    print("A figura é um acutângulo")

elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print("A figura é um obtusângulo")
    
elif ang1 == 90 or ang2 == 90 or ang3 == 90:
    print("A figura é um retângulo")

