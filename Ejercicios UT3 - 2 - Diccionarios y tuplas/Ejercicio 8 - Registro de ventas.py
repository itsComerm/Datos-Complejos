
ventas = {}

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Añadir producto")
    print("2. Añadir registro de venta")
    print("3. Consultar ventas totales")
    print("4. SALIR")

    opcion = input("Selecciona una opción (1-4): ").strip()

    if opcion == "1":
        producto = input("Nombre del producto: ").strip().lower()
        if producto in ventas:
            print("Ese producto ya existe.")
        else:
            ventas[producto] = []
            print(f"Producto '{producto}' añadido correctamente.")

    elif opcion == "2":
        producto = input("Nombre del producto: ").strip().lower()
        if producto not in ventas:
            print("Ese producto no existe. Añádelo primero.")
        else:
            dia = input("Día de la venta: ").strip()
            try:
                unidades = int(input("Unidades vendidas: "))
                ventas[producto].append((dia, unidades))
                print("Registro añadido correctamente.")
            except ValueError:
                print("Error: Debes introducir un número entero para las unidades.")

    elif opcion == "3":
        producto = input("Nombre del producto: ").strip().lower()
        if producto not in ventas:
            print("Ese producto no existe.")
        else:
            total = sum(unidades for dia, unidades in ventas[producto])
            print(f"Total de unidades vendidas de '{producto}': {total}")

    elif opcion == "4" or opcion.upper() == "SALIR":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
