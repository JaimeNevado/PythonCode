nombres = ["Sofia", "Lucas", "Emma"]

try:
    entrada = int(input("Introduce la posición: "))
    print(nombres[entrada])
except IndexError:
    print("Error, índice fuera de rango")