def numero_mayor(num1, num2):
    numero_mayor = 0
    if (num1 > num2):
        numero_mayor = num1
    elif (num1 < num2):
        numero_mayor = num2
    else:
        numero_mayor = 0
    return numero_mayor
numero1 = 20
numero2 = 20
solucion = numero_mayor(numero1, numero2)
print(solucion)

