productos = [
{"Nombre": "Camisa", "Precio base": 20, "Comisión": 5},
{"Nombre": "Pantalón", "Precio base": 30, "Comisión": 7},
{"Nombre": "Zapatos", "Precio base": 50, "Comisión": 10},
{"Nombre": "Bolso", "Precio base": 40, "Comisión": 8},
{"Nombre": "Bufanda", "Precio base": 10, "Comisión": 2}
]

for elemento in productos:
    precioFinal = elemento["Precio base"] + elemento["Comisión"]
    print("El producto:", elemento["Nombre"], "tiene un precio final de", precioFinal, "euros")