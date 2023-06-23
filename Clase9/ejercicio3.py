def suma(nota1, nota2, nota3, nota4):
    return nota1 + nota2 + nota3 + nota4


def media(nota1, nota2, nota3, nota4):
    media = suma(nota1, nota2, nota3, nota4) / 4
    return media

n1 = int(input("Escribe la primera nota: "))
n2 = int(input("Escribe la segunda nota: "))
n3 = int(input("Escribe la tercera nota: "))
n4 = int(input("Escribe la cuarta nota: "))

notaMedia = media(n1, n2, n3, n4)

print("La nota media es:", notaMedia)