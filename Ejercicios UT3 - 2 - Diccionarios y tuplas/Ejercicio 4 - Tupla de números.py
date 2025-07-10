'''Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene
estos números en una tupla. Luego, el programa debe calcular y mostrar la suma, el promedio, el número
máximo y el número mínimo de la tupla.'''

numeros = input("Introduce un listado de numeros separados por comas:").split(",")

tupla = tuple(int(num.strip()) for num in numeros)

sumaTotal = 0
for num in tupla:
    sumaTotal = sumaTotal + num

print(f"El numero promedio es: {sumaTotal/len(tupla)}")
