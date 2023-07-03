try:
    entrada = int(input("Introduce un número: "))
    print(entrada)
except ValueError:
    print("ERROR, solo puedes ingresar números")