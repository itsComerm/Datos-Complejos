'''Escribe un programa que reciba números hasta la introducción de un 0. Por cada número,
suponiendo que el 1 representa el lunes, el 2 el martes, etc., imprime el nombre del día correspondiente.'''

entrada = -1

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

while entrada != 0:
    entrada = int(input("Introduce un numero entero positivo del 1 al 7: "))
    print(dias[entrada-1])
    continue


