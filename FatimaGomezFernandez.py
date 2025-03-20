"""
Mejoras propuestas que no puedo llevar a cabo porque no cumpliría los requisitos:

- Guardar la biblioteca en un archivo a parte. Así se podrían mantener los libros introducidos una vez cerrado el programa
- Usar la función time.sleep al final de cada acción realizada por el usuario. Así no saldría inmediatamente el mensaje de
con las opciones y se le daría tiempo al usuario a revisar los datos que imprime el programa.
"""

#Lista para guardar los objetos libros
biblioteca = []


class Libro():

    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.isbn = ""
        self.disponible = True
        biblioteca.append(self)

    #Función para agregar libro
    def agregar(self):
        self.titulo = (input("Ingrese el título del libro: "))
        self.autor = (input("Ingrese el autor del libro: "))
        self.isbn = (input("Ingrese el ISBN del libro: "))
        print(f"\n"
              f"Título: {self.titulo}"
              f"\n Autor: {self.autor}"
              f"\n ISBN: {self.isbn}"
              f"\n Libro agregado con éxito \n")

    #Función para prestar libro
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print("Libro prestado con éxito \n")
        else:
            print("El libro ya está prestado \n")

    #Función para devolver libro
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print("Libro devuelto con éxito \n")
        else:
            print("Ya se había devuelto este libro anteriormente \n")

    #Función que muestra los datos de todos los libros
    @staticmethod
    def mostrar():
        for libro in biblioteca:
            print(f"{libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {'Sí' if libro.disponible == True else 'No'} \n")

    #Función que busca un libro en concreto y muestra los datos por pantalla de todos los libros
    @staticmethod
    def buscar():
        isbn = (input("Ingresa el ISBN: "))
        libro_encontrado = None

        for libro in biblioteca:
            if libro.isbn == isbn:
                libro_encontrado = libro
                print(f"{libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {'Sí' if libro.disponible == True else 'No'} \n")

        if libro_encontrado == None:
            print('Libro no encontrado \n')

        return libro_encontrado


print("Bienvenido al Sistema de Gestión de Biblioteca")

while True:
    opcion = input("\n 1. Agregar libro "
                   "\n 2. Prestar libro "
                   "\n 6. Salir "
                   "\n Elige una opción: ").strip()
    print("\n")

    # Se crea un objeto de la clase Libro y se llama al metodo agregar
    if opcion == '1':
        nuevo_libro = Libro()
        nuevo_libro.agregar()

    #Esta opción valida que el ISBN del libro que se desea prestar corresponde a un libro agregado a la lista Biblioteca
    #Si existe el libro, le cambiará el estado a "prestado"
    elif opcion == '2':
        libro_prestado = Libro.buscar()
        if libro_prestado != None:
            libro_prestado.prestar()


    elif opcion == '6':
        break
    else:
        print("Opción no válida")

print("Hasta Luego, vuelva pronto a nuestra biblioteca")


