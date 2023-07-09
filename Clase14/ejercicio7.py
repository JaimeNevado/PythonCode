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
    return sol

num = 3
expo = 7
valor = potencia(num, expo)
print("La potencia de", num, "elevado a", expo, "es", valor)