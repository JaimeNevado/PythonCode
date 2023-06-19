# Ejercicio 2

# Lista de alumnos en la clase
clase = ["maria", "juan", "pedro", "ana", "luisa"]

# Solicitar al usuario el nombre del alumno
nombre_alumno = input("Ingrese el nombre del alumno: ")

# Comprobar si el alumno está en la lista
if nombre_alumno.lower() in clase:
    print("El alumno", nombre_alumno, "está en la clase.")
else:
    clase.append(nombre_alumno)
    print("Se ha añadido al alumno", nombre_alumno, "a la clase.")

print("Lista de alumnos en la clase:", clase)


frutas = ["manzana", "plátano", "naranja", "kiwi", "pera"]
longitud = len(frutas)
print(longitud)  # Salida: 5

