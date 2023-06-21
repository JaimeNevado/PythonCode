# Función para saludar
def saludar(nombre):
    print("¡Hola", nombre, "¿Cómo estás?")

# Función para mostrar un mensaje de despedida
def despedir(nombre):
    print("¡Hasta luego", nombre, "Que tengas un buen día.")

# Función principal
n = input("Dime tu nombre: ")
saludar(n)
despedir(n)

