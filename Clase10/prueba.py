def division(a, b):
    resultado = a / b
    print(resultado)

def superImportante():
    print("Soy importante")

try:
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    division(num1, num2)
    superImportante()
except ZeroDivisionError:
    print("Ha habido un error con la division entre 0")
    superImportante()
except ValueError:
    print("Ha habido un error con el valor introducido")
    superImportante()