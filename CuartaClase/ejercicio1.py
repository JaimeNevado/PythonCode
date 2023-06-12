# Ejercicio 1 - Uso de String

# Solicitar al usuario su nombre
nombre = input("Ingrese su nombre: ")

# Solicitar al usuario la posición deseada
posicion = int(input("Ingrese una posición (número entero): "))

# Obtener la letra en la posición indicada
letra = nombre[posicion]

# Mostrar la letra obtenida
print("La letra en la posición", posicion, "es:", letra)