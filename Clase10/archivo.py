import random

colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios = [{'Nombre': 'Josep'}, {'Nombre': 'Claudio'}, {'Nombre': 'Isabel'}, {'Nombre': 'Shella'}]

def eliminar_usuario():
    while True:
        try:
            indice = int(input("Seleccione el usuario que desea eliminar: "))
            if (indice >= 0 and indice < len(usuarios)):
                print("Vamos a eliminar un usuario")
                usuarios.pop(indice)
                print(usuarios)
                return
            else:
                print("No se puede eliminar ese usuario (Error en el número introducido)")
        except ValueError:
            print("Error seleccionando el índice a eliminar")


eliminar_usuario()