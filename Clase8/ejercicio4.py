def suma():
    print("Ha elegido sumar")

def resta():
    print("Ha elegido restar")

def multiplicacion():
    print("Ha elegido multiplicar")

def division():
    print("Ha elegido dividir")

def error():
    print("ERROR. Por favor, selecciona un número del 1 al 4.")

print("¿Qué quieres hacer?")
print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")

opcion = int(input("Introduce el número de la opción elegida: "))

if opcion == 1:
    suma()
elif opcion == 2:
    resta()
elif opcion == 3:
    multiplicacion()
elif opcion == 4:
    division()
else:
    error()