usuarios = [
    {"Nombre": "Juan", "edad": 25},
    {"Nombre": "María", "edad": 30},
    {"Nombre": "Pedro", "edad": 35}
]

for usuario in usuarios:
    usuario["Nombre"] = "Antonio"

# Otro bucle para escribir la nueva lista con los nombres
for usuario in usuarios:
    print(usuario["Nombre"])