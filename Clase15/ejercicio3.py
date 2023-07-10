stock = [
    {"Producto": "Camisa", "Precio": 20},
    {"Producto": "Pantalón", "Precio": 30},
    {"Producto": "Zapatos", "Precio": 50},
    {"Producto": "Bolso", "Precio": 40},
    {"Producto": "Bufanda", "Precio": 10}
]

def encontrar_precio(nombreProducto):
    valor = 0
    for elemento in stock:
        if (elemento["Producto"] == nombreProducto):
            valor = elemento["Precio"]
    return valor

nombreProducto = input("Escribe el nombre del producto: ")
precioProducto = encontrar_precio(nombreProducto)
print("El precio de", nombreProducto, "es", precioProducto, "euros")