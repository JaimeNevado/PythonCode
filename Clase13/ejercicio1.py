stock = [
    {"Producto": "Camisa", "Precio": 20},
    {"Producto": "Pantalón", "Precio": 30},
    {"Producto": "Zapatos", "Precio": 50},
    {"Producto": "Bolso", "Precio": 40},
    {"Producto": "Bufanda", "Precio": 10}
]

for elemento in stock:
    if (elemento["Precio"] < 40):
        print(elemento["Producto"], elemento["Precio"], "EUROS")
