num_jugadores = 4
puntuacion_inicial = 121
num_rondas = 3
ganadores = []

for ronda in range(1, num_rondas + 1):
    print(f"----- Ronda {ronda} -----")

    for jugador in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {jugador + 1}: ")
        puntuacion_ronda = sum(int(input(f"Tirada {i + 1}: ")) for i in range(3))

        if puntuacion_inicial - puntuacion_ronda <= 0:
            ganadores.append(nombre)

        puntuacion_inicial -= puntuacion_ronda

    if ganadores:
        break

if ganadores:
    print("¡Hemos encontrado ganadores!")
    print(f"En la ronda {ronda}, el/los ganador(es) es/son: {', '.join(ganadores)}")
else:
    print("Ningún jugador ha llegado a 0 puntos o menos después de las tres rondas. ¡Sigan jugando!")
