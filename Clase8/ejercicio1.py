# Definición del diccionario
productos = {
    "frutas": {
        "manzanas": 10,
        "bananas": 5,
        "naranjas": 8
    },
    "verduras": {
        "zanahorias": 15,
        "lechugas": 7,
        "tomates": 12
    }
}

# Accediendo a los elementos del diccionario
print("Cantidad de manzanas:", productos["frutas"]["manzanas"])
print("Cantidad de zanahorias:", productos["verduras"]["zanahorias"])
print("Cantidad de naranjas:", productos["frutas"]["naranjas"])
print("Cantidad de lechugas:", productos["verduras"]["lechugas"])
