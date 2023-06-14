# Ejercicio 3 - Iteracion de Listas

# Creación de listas
alumnos = ["María", "Antonio", "Carmen", "Manuel", "Ana", "Francisco", "Laura", "David", "Isabel", "Javier"]
notas = [8, 7, 6, 9, 10, 5, 8, 7, 9, 6]

#Declaración de variable de contador
var1 = 0
while (var1 < 10):
	#Repetimos 10 veces el print con valores de var1 distintos
	print("La nota de", alumnos[var1],"es", notas[var1])
	var1 = var1 + 1
