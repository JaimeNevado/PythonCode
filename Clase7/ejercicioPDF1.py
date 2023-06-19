import random

colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios = [{'Nombre': 'Josep'}, {'Nombre': 'Claudio'}, {'Nombre': 'Isabel'}, {'Nombre': 'Shella'}]

def agregar_color():
    while True:
        color = input("Ingresa un color para agregar a la lista (escribe 'salir' para finalizar): ")
        if color.lower() == 'salir':
            break
        if color.lower() not in colores:
            colores.append(color.lower())
            print(f"El color '{color}' fue agregado a la lista.")
        else:
            print(f"El color '{color}' ya existe en la lista.")

def mostrar_colores():
    print("Listado de colores:")
    for color in colores:
        print(color)

def ordenar_colores():
    colores.sort()
    print("Listado de colores ordenado alfabéticamente:")
    for color in colores:
        print(color)

def asignar_colores():
    if len(colores) < len(usuarios):
        print("No hay suficientes colores para asignar a todos los usuarios.")
        return
    for usuario in usuarios:
        color = random.choice(colores)
        usuario['Color'] = color
        colores.remove(color)
        print(f"Se asignó el color '{color}' al usuario {usuario['Nombre']}.")

def eliminar_usuario():
    while True:
        try:
            indice = int(input("Ingrese el índice del usuario a eliminar (0-{}): ".format(len(usuarios)-1)))
            if 0 <= indice < len(usuarios):
                usuario_eliminado = usuarios.pop(indice)
                print(f"El usuario {usuario_eliminado['Nombre']} fue eliminado.")
                break
            else:
                print("Índice inválido. Inténtelo nuevamente.")
        except ValueError:
            print("Valor inválido. Inténtelo nuevamente.")

def mostrar_usuarios_ordenados():
    usuarios_ordenados = sorted(usuarios, key=lambda x: x['Nombre'])
    print("Usuarios ordenados alfabéticamente:")
    for usuario in usuarios_ordenados:
        print(usuario['Nombre'])

def mostrar_nombres_usuarios():
    print("Listado de usuarios:")
    for usuario in usuarios:
        print(usuario['Nombre'])

def salir():
    print("¡Hasta luego!")
    exit()

def mostrar_menu():
    print("---- MENÚ ----")
    print("1. Agregar colores a la lista")
    print("2. Mostrar listado de colores")
    print("3. Ordenar listado de colores alfabéticamente")
    print("4. Asignar colores a cada usuario de manera aleatoria")
    print("5. Eliminar usuario")
    print("6. Mostrar usuarios ordenados alfabéticamente")
    print("7. Mostrar usuarios solo con el Nombre")
    print("8. Salir")

acciones = {
    '1': agregar_color,
    '2': mostrar_colores,
    '3': ordenar_colores,
    '4': asignar_colores,
    '5': eliminar_usuario,
    '6': mostrar_usuarios_ordenados,
    '7': mostrar_nombres_usuarios,
    '8': salir
}

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la acción que desea realizar: ")

    if opcion in acciones:
        acciones[opcion]()
    else:
        print("O");
