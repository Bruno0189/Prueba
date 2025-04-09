# Clase.
libros = []

# Funcion para mostrar las opciones.
def elecciones():
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar")
    print("6. Salir")
    
# Usamos el while True para que el programa se ejecute hasta que el usuario decida salir
while True:
    elecciones()
    # Mediante un input se le pide al usuario elegir una opción. 
    opcion = input("Elige una opción: ")
    
    # Realizamos un .append para agregar un libro. 
    if opcion == '1':
        print("\nAgregar libro:")
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        libros.append({"titulo": titulo, "autor": autor, "isbn": isbn})
        print("Nuevo libro agregado con éxito.")
        
    # Realizamos un .remove para prestar un libro.    
    elif opcion == '2':
        print("Prestar libro: ")
        isbn= input("Ingrese el ISBN del libro: ")
        for libro in libros:
            if libro[isbn]==isbn:
                libros.remove(libro)
                print("Libro presado con éxito.")
            
    # Realizamos un .append para devolver el libro.        
    elif opcion == '3':
        print("Devolver el libro: ")
        titulo= input("Ingrese el titulo del libro que desea devolver: ")
        autor= input("Ingrese el autor del libro que quiera devolver: ")
        isbn= input("Ingrese el ISBN del libro que quiera devolver: ")
        libros.append({"titulo": titulo, "autor": autor, "isbn": isbn})
        print("Libro devuleto con éxito.")
    
    # Realizamos un for in (i) para mostrar los libros.    
    elif opcion == '4':
        print("\nListado de libros:")
        for libro in libros:
            print(f"- {libro['titulo']} ({libro['autor']}) - ISBN: {libro['isbn']}")
            
    # Realizamos un for in (i) para buscar un libro.       
    elif opcion == '5':
        print("Buscar libro: ")
        busqueda = input("Ingrese el ISBN del libro: ")
        for libro in libros:
            if libro[libro]==busqueda:
                print(f"El libro con ISBN {busqueda} fue encontrado.")
                
    # Realizamos un break para salir del programa.             
    elif opcion == '6':
        print("¡Hasta luego!")
        break
    
    # Realizamos un else para las respuestas que no estan en las opciones.    
    else:
        print("\nOpción incorrecta. Inténtalo de nuevo.")
        