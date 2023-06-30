usuarios = [
    {"Nombre": "Juan", "edad": 25},
    {"Nombre": "María", "edad": 30},
    {"Nombre": "Pedro", "edad": 35}
]

def sumar_edades():
    suma=0
    for diccionario_suma in usuarios:
        suma= suma+ diccionario_suma["edad"]
    print("La suma de las edades es ", suma)

def agregar_usuarios():
    usuarios.append({"Nombre": "Laura", "edad": 28} )

def escribir_usuarios():
    for usuario in usuarios:
        print (usuario["Nombre"], usuario["edad"])

# Declaracion de la funcion
def eliminar_usuarios(usr):
    usuarios.remove(usr)


# Codigo de fuera o llamada
user = {"Nombre": "Juan", "edad": 25}
eliminar_usuarios(user)
escribir_usuarios()
