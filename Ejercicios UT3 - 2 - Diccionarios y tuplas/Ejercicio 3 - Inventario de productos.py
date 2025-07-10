'''Escribe un programa que gestione un inventario de productos utilizando un diccionario. El programa debe permitir al usuario
 añadir productos con su nombre y cantidad, eliminar productos, y consultar la cantidad de un producto específico. El programa
 debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".'''

inventario = {
    "camiseta": 5,
    "pantalon":3,
}

accion = 0
while accion != 4:
    if accion == 0:
        print("PROGRAMA DE GESTIÓN DE INVENTARIO")
        print("Menu de navegación")
        print("1: Añadir productos")
        print("2: Eliminar productos")
        print("3: Consultar stock")
        accion = int(input("Que acción quiere realizar? "))


    if accion > 4:
        print("Operación no disponible, selecciona otra.")
        print("Menu de navegación")
        print("1: Añadir productos")
        print("2: Eliminar productos")
        print("3: Consultar stock")
        print("4: Salir")
        accion = int(input("Que acción quiere realizar? "))

    if accion == 1:
        print("Añadir producto al inventario.")
        nombreArticulo = input("Introduce el nombre del producto: ").strip().lower()


        if nombreArticulo in inventario:
            cantidadArticulo = int(input("Articulo ya existente, cuanto quieres añadir al stock? "))
            inventario[nombreArticulo] += cantidadArticulo
            print("-------------------------------")
            print("CANTIDAD AÑADIDA CORRECTAMENTE!")
            print(f"Resumen: Se han añadido {cantidadArticulo} unidad/es al articulo {nombreArticulo}. Ahora tiene un total de {inventario[nombreArticulo]} unidad/es.")
            print("-------------------------------")
            print("")

        else:
            cantidadArticulo = int(input("Nuevo producto creado. Que cantidad quieres añadir? "))
            inventario[nombreArticulo] = cantidadArticulo
            print("")
            print("-------------------------------")
            print("PRODUCTO CREADO CORRECTAMENTE!")
            print(f"Resumen: Se ha añadido {nombreArticulo} al inventario con {cantidadArticulo} unidad/es de producto.")
            print("-------------------------------")
            print("")

        print("Desea realizar otra gestión?")
        print("----------------------------------------------------------------------------")
        print("1: Añadir productos | 2: Eliminar productos | 3: Consultar stock | 4: Salir")
        print("----------------------------------------------------------------------------")
        accion = int(input("Que acción quiere realizar? "))
        continue

    if accion == 2:
        print("Eliminar producto del inventario.")
        nombreArticulo = input("Introduce el nombre del producto: ").strip().lower()

        if nombreArticulo in inventario:

            del inventario[nombreArticulo]

            print("-------------------------------")
            print("PRODUCTO ELIMINADO CORRECTAMENTE!")
            print("-------------------------------")
            print("")

        else:
            print("ERROR: Producto no encontrado.")
            print("")
        print("Desea realizar otra gestión?")
        print("----------------------------------------------------------------------------")
        print("1: Añadir productos | 2: Eliminar productos | 3: Consultar stock | 4: Salir")
        print("----------------------------------------------------------------------------")
        accion = int(input("Que acción quiere realizar? "))
        continue

    if accion == 3:
        print("")
        print("-------------------------------")
        print("INVENTARIO ACTUAL:")
        print("")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad} unidades")
        print("-------------------------------")
        print("")

        print("Desea realizar otra gestión?")
        print("----------------------------------------------------------------------------")
        print("1: Añadir productos | 2: Eliminar productos | 3: Consultar stock | 4: Salir")
        print("----------------------------------------------------------------------------")
        accion = int(input("Que acción quiere realizar? "))
        continue
    if accion == 4:
        print("Cerrando sesión...")
        break