stock = [
    {"Producto": "Camisa", "Precio": 20},
    {"Producto": "Pantalón", "Precio": 30},
    {"Producto": "Zapatos", "Precio": 50},
    {"Producto": "Bolso", "Precio": 40},
    {"Producto": "Bufanda", "Precio": 10}
]

def media_precios(stock):
    suma = 0
    numero_productos = 0
    for elemento in stock:
        suma = suma + elemento["Precio"]
        numero_productos = numero_productos + 1

    media = suma / numero_productos
    return media

print("La media de los precios del stock es:", media_precios(stock))