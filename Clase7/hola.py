# Tienda

dic = {"piña" : 4, "manzana" : 0, "melocoton" : 7, "agua" : 10}

eleccion = input("¿Que quiere comprar?: ")

if eleccion.lower() in dic:
    if dic[eleccion.lower()] <= 0:
        print("No quedan ", eleccion.lower())
    else:
        print("Hay", eleccion.lower())
        dic[eleccion.lower()] = dic[eleccion.lower()] - 1
    
else:
    print("No hay", eleccion.lower()) 

print(dic)