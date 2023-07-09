def calcularIVA(precio, iva):
    precioFinal = precio + (precio * (iva/100))
    return precioFinal

precioBase = 10
iva = 10
print("El precio base es", precioBase, "y el IVA es del", iva, "%")
print("Valor final:", calcularIVA(precioBase, iva))