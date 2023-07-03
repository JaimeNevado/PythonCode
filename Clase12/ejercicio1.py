empleados = [
    {"Nombre": "Juan", "Edad": 25},
    {"Nombre": "María", "Edad": 30},
    {"Nombre": "Carlos", "Edad": 28},
    {"Nombre": "Laura", "Edad": 35},
    {"Nombre": "Pedro", "Edad": 27}
]

for empleado in empleados:
    if (empleado["Edad"] < 30):
        print(empleado["Nombre"], empleado["Edad"])