empleados = [
    {"Nombre": "Juan", "Edad": 25},
    {"Nombre": "María", "Edad": 30},
    {"Nombre": "Carlos", "Edad": 28},
    {"Nombre": "Laura", "Edad": 35},
    {"Nombre": "Pedro", "Edad": 27}
]

print("Lista original:")
# Código para escribir el diccionario
for elemento in empleados:
    print(elemento["Nombre"], elemento["Edad"])


nombre_a_cambiar = input("Introduce el nombre que deseas cambiar: ")
for empleado in empleados:
    if (nombre_a_cambiar == empleado["Nombre"]):
        empleado["Nombre"] = "Arturo"
    else:
        empleado["Nombre"] = nombre_a_cambiar

print("Lista cambiada:")
# Código para escribir el diccionario
for elemento in empleados:
    print(elemento["Nombre"], elemento["Edad"])