try:
    numero_posicion=int(input("Introduce un numero: "))
    nombres = ["Sofia", "Lucas", "Emma"]
    if (numero_posicion < 0):
        raise IndexError
    print (nombres[numero_posicion])
except IndexError:
    print("Error, índice fuera de rango")
except ValueError:
    print("Solo se puede introducir numeros")