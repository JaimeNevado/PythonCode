def division():
    dividendo = 3
    divisor = 0
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")

def rango():
    lista = ["juan"]
    indice = 3
    try:
        elemento = lista[indice]
    except IndexError:
        print("Error: El índice está fuera del rango de la lista.")

def conversion():
    letra = "c"
    try:
        numero = int(letra)
    except ValueError:
        print("Error: No se pudo convertir el valor a un entero.")
