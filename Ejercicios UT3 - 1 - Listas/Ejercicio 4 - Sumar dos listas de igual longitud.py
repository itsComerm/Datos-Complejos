'''Escribe un programa que pida al usuario dos listas de números enteros separados por comas
y sume los elementos de ambas listas. El programa debe imprimir la lista resultante.
Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.'''

print("Vamos a sumar las dos listas. (Ambas deben tener la misma longitud)")
lista1 = input("Introduce los numeros de la lista 1: ").split(",")
longitud = (len(lista1))
lista2 = input("Introduce ahora los " + str(longitud) + " dígitos para la lista 2: ").split(",")

if len(lista1) != len(lista2) :
    print("Las listas deben tener la misma cantidad de dígitos.")
else:
    lista_resultado = []
    for i in range (len(lista1)):
        lista_resultado.append(int(lista1[i])+int(lista2[i]))

print("La lista resultado es: " , lista_resultado)
