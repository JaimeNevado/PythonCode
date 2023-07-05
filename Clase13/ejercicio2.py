stock = [
    {"Producto": "Camisa", "Precio": 20},
    {"Producto": "Pantalón", "Precio": 30},
    {"Producto": "Zapatos", "Precio": 50},
    {"Producto": "Bolso", "Precio": 40},
    {"Producto": "Bufanda", "Precio": 10}
]

entrada = input("Tienes descuento (si/no): ")
try:
    if (entrada.lower() == "si"):
        for elemento in stock:
            elemento["Precio"] = elemento["Precio"] - 5
    elif(entrada.lower() != "no"):
        raise ValueError
    for elemento in stock:
        print(elemento["Producto"], elemento["Precio"], "EUROS")
except ValueError:
    print("Solo puedes poner Si o No")