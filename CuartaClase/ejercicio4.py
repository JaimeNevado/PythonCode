# Ejercicio 4 - Calculadora en Python

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú de opciones
print("OPERACIONES POSIBLES:")
print("1 Sumar los dos números.")
print("2 Restar el segundo número al primero.")
print("3 Multiplicar los dos números.")
print("4 Dividir el primer número entre el segundo.")

# Solicitar al usuario que seleccione una opción
opcion = int(input("Elija una operación (1-4): "))

# Realizar la operación correspondiente y mostrar el resultado
if (opcion == 1):
    resultado = num1 + num2
    print("Solución: ", resultado)
elif opcion == 2:
    resultado = num1 - num2
    print("Solución: ", resultado)
elif opcion == 3:
    resultado = num1 * num2
    print("Solución: ", resultado)
elif opcion == 4:
    # Este if comprueba que el num2 no sea 0 para realizar la division
    if num2 != 0:
        resultado = num1 / num2
        print("Solución: ", resultado)
    else:
        # Si el num2 es 0, no se puede dividir entre cero
        print("No se puede dividir entre cero.")
else:
    print("Opción no válida.")

