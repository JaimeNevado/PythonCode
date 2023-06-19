
# Crear una lista
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# Lista notas finales
notas = [10, 9, 8, 6, 4, 7, 10, 5, 3, 10, 2, 1, 10, 7, 9, 10, 8, 6]

print("Hay ", notas.count(10), "notas con un 10 entre los ", len(notas))

nuevo = input("Introduce un nuevo día: ")

dias.sort()

if nuevo.lower() in dias:
    print("Si está en la lista")
else:
    print("No está en la lista")
    
# Imprimir la lista
print("Lista:", dias)
