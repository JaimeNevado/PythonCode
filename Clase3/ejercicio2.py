'''
Haz un programa que solicite al usuario ingresar su peso en kilogramos
y su altura en metros. El programa deberá calcular el índice de masa corporal 
(IMC) utilizando la fórmula IMC = peso / (altura*altura). 
A continuación, mostrará el valor del IMC y un mensaje con print 
según el rango en el que se encuentra el IMC, de acuerdo a la siguiente 
clasificación:

Menor a 18.5: 'Tiene un peso bajo.'
Entre 18.5 y 24.9: 'Su peso está dentro del rango normal.'
Entre 25 y 29.9: 'Tiene sobrepeso.'
30 o mayor: 'Tiene obesidad.'

Usa la estructura if para determinar el rango y utilizar input y print 
para obtener y mostrar los resultados.
'''

# Solicitar el peso y la altura al usuario
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (altura * altura)

# Mostrar el resultado del IMC con un mensaje correspondiente
print("Su índice de masa corporal (IMC) es:", imc)

if imc < 18.5:
    print("Tiene un peso bajo.")
elif imc < 25:
    print("Su peso está dentro del rango normal.")
elif imc < 30:
    print("Tiene sobrepeso.")
elif imc >= 30:
    print("Tiene obesidad.")

