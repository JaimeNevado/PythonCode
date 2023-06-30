usuarios = [
    {"Nombre": "Juan", "edad": 25},
    {"Nombre": "María", "edad": 30},
    {"Nombre": "Pedro", "edad": 35}
]

suma = 0
for usuario in usuarios:
    suma = suma + usuario["edad"]

print("La suma de las edades es:", suma)