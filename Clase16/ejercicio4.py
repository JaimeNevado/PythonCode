
def crearClase(alumnos):
    contador = 0
    clase1 = []
    clase2 = []
    for elemento in alumnos:
        if (contador % 2 == 0):
            clase1.append(elemento)
        else:
            clase2.append(elemento)
        contador = contador + 1

    print("La primera clase es:")
    print(clase1)
    print("La segunda clase es:")
    print(clase2)

#Lista de alumnos
alumnos = ["Juan", "María", "Pedro", "Laura", "Ana", "Carlos", "Sofía", "Alejandro"]

crearClase(alumnos)


