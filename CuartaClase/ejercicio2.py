# Ejercicio 2 - Rango de edades

# Solicitar la edad al usuario
edad = int(input("Escriba su edad: "))

# Determinar el grupo de edad
if edad < 0:
    print("ERROR La edad ingresada no es válida.")
elif edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres mayor de edad.")
else:
    print("Eres un jubilado.")
