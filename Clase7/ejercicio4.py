# Ejercicio 4, Amazon

stock = {
    'iphone': {'cantidad': 10, 'precio': 1000},
    'macbook': {'cantidad': 5, 'precio': 2000},
    'airpods': {'cantidad': 20, 'precio': 200},
}

productos_potenciales = []

# Ejemplo de uso del programa
producto = input("Ingrese el nombre del producto que desea comprar: ")

if producto.lower() in stock:
    if stock[producto]['cantidad'] > 0:
        stock[producto]['cantidad'] = stock[producto]['cantidad'] - 1
        print("Producto comprado:", producto)
    else:
        print("No quedan productos.")
else:
    productos_potenciales.append(producto)
    print("Producto añadido a la lista de productos potenciales: ", producto)

print("----------------------------")
print("Lista de productos en stock:")
print(stock)
print("----------------------------")
print("Lista de productos potenciales:")
print(productos_potenciales)
print("----------------------------")