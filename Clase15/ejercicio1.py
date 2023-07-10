def potencia(num, expo):
    sol = 0
    if (expo > 0 and expo < 5):
        if (expo == 1):
            sol = num
        elif (expo == 2):
            sol = num * num
        elif (expo == 3):
            sol = num * num * num
        elif (expo == 4):
            sol = num * num * num * num
    else:
        raise ValueError
    return sol
    
try:
    num = int(input("Introduze el número a elevar: "))
    expo = int(input("Introduze el exponente: "))
    valor = potencia(num, expo)
    print("La potencia de", num, "elevado a", expo, "es", valor)
except ValueError:
    print("El exponente debe ser mayor que 0 y menor que 5")