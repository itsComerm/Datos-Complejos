'''Escribe un programa que gestione una biblioteca digital utilizando un diccionario. El programa debe permitir
al usuario añadir libros con su título, autor y año de publicación. El usuario debe poder consultar los libros
por autor o por año de publicación. El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".'''

libros = {
    "Padre rico, padre pobre": {
        "autor": "Robert T. Kiyosaki",
        "año": 1997
    },
    "El hombre en busca de sentido": {
        "autor": "Viktor Frankl",
        "año": 1946
    },
    "Los secretos de la mente millonaria": {
        "autor": "T. Harv Eker",
        "año": 2005
    },
}

accion = 0
while accion != 4:
    if accion == 0:
        print("----------------------------------")
        print("BIENVENIDO A LA BIBLIOTECA ONLINE!")
        print("----------------------------------")
        print("Menu de navegación")
        print("")
        print("1: Añadir libro")
        print("2: Buscador de libros")
        print("----------------------------------")
        accion = int(input("Que acción quiere realizar? "))


    if accion > 3:
        print("------------------------------------------")
        print("Operación no disponible, selecciona otra.")
        print("---------------------------------------------------")
        print("1: Añadir libro | 2: Buscar un libro | 3: Salir")
        print("---------------------------------------------------")
        accion = int(input("Que acción quiere realizar? "))

    if accion == 1:
        print("Añadir libro a la biblioteca.")
        nombrelibro = input("Introduce el nombre del libro: ").strip().lower()

        if nombrelibro in libros:
            print("Este libro ya existe en la biblioteca.")
            print("Desea realizar otra gestión?")
            print("----------------------------------------------------------------------------")
            print("1: Añadir productos | 2: Buscar un libro | 3: Salir")
            print("----------------------------------------------------------------------------")
            accion = int(input("Que acción quiere realizar? "))
            continue
        else:
            autor = input("Introduce el autor del libro: ")
            anoPublicacion = int(input("Introduce el año de publicación: "))
            print(libros)
            libros[nombrelibro] = {
                "autor": autor,
                "año": anoPublicacion
            }
            print("")
            print("-------------------------------")
            print("LIBRO AÑADIDO CORRECTAMENTE!")
            print(f"Resumen: Se ha añadido el libro {nombrelibro} a la biblioteca.")
            print("-------------------------------")
            print("")

        print("Desea realizar otra gestión?")
        print("----------------------------------------------------------------------------")
        print("1: Añadir productos | 2: Buscar un libro | 3: Salir")
        print("----------------------------------------------------------------------------")
        accion = int(input("Que acción quiere realizar? "))
        continue

    if accion == 2:
        print("Menu de opciones de busqueda")
        print("----------------------------------------------------------------------------")
        print("1: Por autor | 2: Por año | 3: Volver al menú")
        print("----------------------------------------------------------------------------")
        modoBusqueda = int(input("Como quieres buscar? "))
        if modoBusqueda == 1:
            autor = input("Introduce el nombre del autor: ").strip().lower()
            encontrados = False
            for libro, escritor in libros.items():
                if autor in escritor["autor"].lower():
                    print(f"Título: {libro.title()} | Autor: {escritor['autor']} | Año: {escritor['año']}")
                    encontrados = True
            if not encontrados:
                print("No se encontraron libros con ese autor.")
                print("")
                print("Desea realizar otra gestión?")
                print("----------------------------------------------------------------------------")
                print("1: Añadir libro | 2: Buscar un libro | 3: Salir")
                print("----------------------------------------------------------------------------")
                accion = int(input("Que acción quiere realizar? "))

        if modoBusqueda == 2:
            fecha = int(input("Introduce la fecha de publicación: "))
            encontrados = False
            for libro, fechaa in libros.items():
                if fecha == fechaa["año"]:
                    print(f"Título: {libro.title()} | Autor: {fechaa['autor']} | Año: {fechaa['año']}")
                    encontrados = True
            if not encontrados:
                print("No se encontraron libros con esa fecha.")
                print("")
                print("Desea realizar otra gestión?")
                print("----------------------------------------------------------------------------")
                print("1: Añadir libro | 2: Buscar un libro | 3: Salir")
                print("----------------------------------------------------------------------------")
                accion = int(input("Que acción quiere realizar? "))

    if accion == 3:
        print("Cerrando sesión...")
        break