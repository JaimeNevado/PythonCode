'''
Crea un programa con una variable llamada numeroSecreto y pregunta al usuario
¿Cuál es el número secreto? y mientras no lo acierten, el programa sigue 
preguntando al usuario hasta que acierten el numero.
Cuando acierten, el programa debe parar y escribir "Has acertado"

Usa while, input, print
'''

numeroSecreto = 42

numeroIntroducido = int(input("¿Cuál es el número secreto?: "))

variable = 12
variable = 13

while numeroSecreto != numeroIntroducido:
    numeroIntroducido = int(input("¿Cuál es el número secreto?: "))

print("Has acertado el numero secreto ;)")
