class Amigo:
    def __init__(self, nombre, dni, poblacion):
        self.nombre = self._capitalizar_palabras(nombre)
        self.dni = self._validar_dni(dni)
        self.poblacion = self._capitalizar_palabras(poblacion)

    def _capitalizar_palabras(self, texto):
        palabras = texto.lower().split()
        palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
        return ' '.join(palabras_capitalizadas)

    def _validar_dni(self, dni):
        if len(dni) != 9 or not dni[:-1].isalnum() or not dni[-1].isalpha():
            raise ValueError("El DNI debe tener 9 caracteres alfanuméricos y la última posición debe ser una letra.")
        return dni

    def mostrar_datos(self):
        print("Datos del amigo:")
        print("Nombre y apellidos:", self.nombre)
        print("DNI:", self.dni)
        print("Población:", self.poblacion)


class GustosMusicales(Amigo):
    def __init__(self, nombre, dni, poblacion, cancion_favorita, grupo, estilo_musical):
        super().__init__(nombre, dni, poblacion)
        self.cancion_favorita = cancion_favorita
        self.grupo = grupo
        self.estilo_musical = estilo_musical.upper()

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Gustos musicales:")
        print("Canción favorita:", self.cancion_favorita)
        print("Grupo:", self.grupo)
        print("Estilo musical:", self.estilo_musical)


# Ejemplo de uso
nombre = input("Nombre y apellidos: ")
dni = input("DNI: ")
poblacion = input("Población: ")
cancion_favorita = input("Canción favorita: ")
grupo = input("Grupo: ")
estilo_musical = input("Estilo musical: ")

amigo = GustosMusicales(nombre, dni, poblacion, cancion_favorita, grupo, estilo_musical)
amigo.mostrar_datos()
