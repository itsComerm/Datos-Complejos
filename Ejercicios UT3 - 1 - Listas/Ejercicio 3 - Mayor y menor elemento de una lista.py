'''Ejercicio 3 - Mayor y menor elemento de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados
por comas y encuentre el mayor y el menor elemento de la lista.
El programa debe imprimir ambos resultados.'''

elementos = input("Introduce una lista de números enteros separados por comas: ").split(",")

print(elementos)

'''Encontrar elementos con la funcion min y max:'''

print(min(elementos))
print(max(elementos))

'''Encontrar elementos con la funcion sort y por posición:'''

elementos.sort()
print(elementos)

print("El número más pequeño es:", elementos[0])
print("El número más pequeño es:", elementos[len(elementos)-1])




