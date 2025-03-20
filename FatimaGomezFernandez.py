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
            print("Se te ha prestado el libro, recuerda devolverlo en plazo \n")
        else:
            print("El libro ya está prestado \n")

    #Función para devolver libro
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print("Has devuelto el libro correctamente \n")
        else:
            print("Ya se había devuelto este libro anteriormente \n")

#Función que muestra por pantalla los datos de un solo libro
def imprimir_informacion(titulo, autor, isbn, disponible):
    print(f"{titulo} ({autor}) - ISBN: {isbn} - Disponible: {'Sí' if disponible == True else 'No'} \n")

#Función que muestra los datos de todos los libros
def mostrar():
    for libro in biblioteca:
        imprimir_informacion(libro.titulo, libro.autor, libro.isbn, libro.disponible)

#Función que busca un libro en concreto y muestra los datos por pantalla de todos los libros
def buscar():
    isbn = (input("Introduzca el ISBN del libro: "))
    libro_encontrado = None

    for libro in biblioteca:
        if libro.isbn == isbn:
            libro_encontrado = libro
            imprimir_informacion(libro.titulo, libro.autor, libro.isbn, libro.disponible)

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
        libro_prestado = buscar()
        if libro_prestado != None:
            libro_prestado.prestar()
        else:
            print('Libro no encontrado \n')


    elif opcion == '6':
        break
    else:
        print("Opción no válida")

print("Hasta Luego, vuelva pronto a nuestra biblioteca")


