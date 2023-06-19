# Ejercicio 3

# Lista de números
numeros = [7, 2, 9, 5, 2, 3, 7, 1, 9, 4, 2, 7]

# Imprimir la lista original
print("Lista original:", numeros)

# Reverse
numeros.reverse()
print("Lista después de aplicar reverse():", numeros)

# Sort
numeros.sort()
print("Lista después de aplicar sort():", numeros)

# Count
numero = 2
ocurrencias = numeros.count(numero)
print("El número", numero, "aparece", ocurrencias, "veces en la lista.")

# Len
longitud = len(numeros)
print("La longitud de la lista es:", longitud)
