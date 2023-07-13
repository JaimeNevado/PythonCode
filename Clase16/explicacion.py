numeros = [1, 2, 5, 6, 7, 10, 4, 10]

def calcularSuma(n):
    suma = 0
    for elemento in n:
        suma = suma + elemento
    return suma

def calcularTamaño(lista):
    tamaño = 0
    for elemento in lista:
        tamaño = tamaño + 1
    return tamaño

def calcularMedia(num):
    resultado = calcularSuma(num) / calcularTamaño(num)
    return resultado


media = calcularMedia(numeros)
print(media)