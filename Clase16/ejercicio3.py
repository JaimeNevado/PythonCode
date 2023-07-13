numeros = [1, 4, 2, 6, 7, 8, 9, 16, 12, 1, 5]

def crearLista(numeros):
    numeros_pares = []
    numeros_impares = []
    for elemento in numeros:
        if (elemento % 2 == 0):
            numeros_pares.append(elemento)
        else:
            numeros_impares.append(elemento)

    # Imprimir lista numeros
    print("Lista pares: ")
    print(numeros_pares)
    print("Lista impares: ")
    print(numeros_impares)

crearLista(numeros)