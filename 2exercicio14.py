#14

i = float(input("digite seu consumo industrial: "))
c = float(input("digite seu consumo comercial: "))
r = float(input("digite seu consumo residencial: "))

if i > 0:
    ci = ( 0.68 * i ) + 34
    print(ci)
elif c > 0:
    cc = ( 0.37 * c ) + 45
    print(cc)
elif r > 0:
    cr = ( 0.77 * r  ) - 22
    print(cr)
