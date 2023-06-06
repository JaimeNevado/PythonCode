'''
Escribe un programa que pida al usuario dos números. 
El programa deberá comparar los números y mostrar un mensaje 
indicando si el primer número es mayor, menor o igual al segundo número. 

Usa if para realizar la comparación, input para preguntar los valores 
y print para escribir.

'''

# Solicitar dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Comparar los números y mostrar el resultado
if (num1 > num2):
    print("El primer número es mayor que el segundo número.")
elif (num1 < num2):
    print("El primer número es menor que el segundo número.")
else:
    print("Ambos números son iguales.")