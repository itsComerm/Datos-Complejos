'''Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto.
El programa debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas
frecuencias. Ignora la puntuación y considera las palabras en minúsculas.'''

palabras = {}

frase = input("Introduce una frase: ").lower().split()
print(frase)

for palabra in frase:
    if palabra in palabras :
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

print(palabras)


