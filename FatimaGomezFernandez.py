biblioteca = []

class Libro():

    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.isbn = ""
        self.disponible = True
        biblioteca.append(self)

    def agregar(self):
        self.titulo = str(input("Ingrese el título del libro: "))
        self.autor = str(input("Ingrese el autor del libro: "))
        self.isbn = str(input("Ingrese el ISBN del libro: "))

    def prestar(self):
        if self.disponible == True:
            self.disponible = False
        else:
            print("No se puede prestar")

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
        else:
            print("El libro ya está devuelto")

def mostrar():
    for libro in biblioteca:
        print(libro.titulo, libro.autor, libro.isbn, libro.disponible)

prueba = Libro()
prueba.agregar()

prueba2 = Libro()
prueba2.agregar()

mostrar()

print('fin')