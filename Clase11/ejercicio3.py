numeros = [1, 2, 3, 4, 5]

# Se inicia en 1 porque si es 0, da siempre 0
multiplicacion = 1
for elemento in numeros:
    multiplicacion = multiplicacion * elemento

print("La multiplicacion es", multiplicacion)