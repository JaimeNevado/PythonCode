''' 
	Haz un programa que pregunte al usuario su salario bruto.
    Con ese dato, calcule sueldo neto y el IRPF cobrado y
    muéstrelo por pantalla.

    Fórmulas:
    IRPF = 0.21 * SalarioBruto
    sueldoFinal = sueldoBruto - IRPF
    
    Debe ver si el nombre es Juanjo, si el nombre es Juanjo,
    no tiene que pagar IRPF.
    
    
    Ejemplo de salida:
    
    "
	Tu nombre de usuario es: <nombre>
    Tu sueldo bruto es: <sueldoBruto>
    Tu sueldo final es: <sueldoFinal>
    Tu retención de IRPF: <impuesto>
    "
    
    Además, gestione los posibles errores en los datos de entrada. (Si el salario es negativo)
	
'''

nombre = input ('Escriba su nombre: ')
bruto = input('Escriba su salario bruto: ')

if (int(bruto) < 0):
    print('Has añadido un valor negativo')
else:
	iva = 0.21 * int(bruto)
	neto = int(bruto) - iva
	if (nombre == 'Juanjo'):
		iva = 0
		neto = int(bruto)
	print("Tu nombre de usuario es: " + nombre)
	print("Tu sueldo bruto es: ", bruto)
	print("Tu sueldo final es: " + str(neto))
	print("Tu comision de IVA: " + str(iva))



