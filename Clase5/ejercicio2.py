# Ejercicio 2 - Modificacion de Listas

amigos = []  # Crear una lista vacía llamada "amigos"

# Pedir al usuario que ingrese 3 nombres y agregarlos a la lista "amigos"
nombre = input("Ingresa el primer nombre: ")
amigos.append(nombre)

nombre = input("Ingresa el segundo nombre: ")
amigos.append(nombre)

nombre = input("Ingresa el tercer nombre: ")
amigos.append(nombre)

print("¿Desea añadir más amigos o desea eliminar alguno?")
print("1) Añadir amigo")
print("2) Eliminar amigo")

respuesta = int(input("Elija 1 o 2: "));

if (respuesta == 1):
    nombre = input("Nombre del amigo para añadir: ")
    amigos.append(nombre)
elif (respuesta == 2):
    nombre = input("Nombre del amigo para eliminar: ")
    amigos.remove(nombre)
else:
    print("Error, los números tienen que ser 1 o 2")

# Imprimir la lista de amigos
print("Lista de amigos final:", amigos)
