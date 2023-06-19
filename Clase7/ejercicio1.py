# Ejercicio 1

# Lista de números
numeros = [2, 5, 8, 10, 13, 15, 18]

# Solicitar al usuario un número
numero_buscado = int(input("Ingrese un número: "))

# Comprobar si el número se encuentra en la lista
if numero_buscado in numeros:
    print("El número", numero_buscado, "se encuentra en la lista.")
else:
    print("El número", numero_buscado, "no se encuentra en la lista.")
