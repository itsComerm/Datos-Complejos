'''Escribe un programa que replique el comportamiento del ejercicio 1, pero en lugar de buscar por clave (
país), el usuario debe poder buscar por valor (capital). El programa debe permitir al usuario introducir
una capital y devolver el país correspondiente. Si la capital no está en el diccionario, el programa debe
informar al usuario.
'''
from tkinter.font import names

paises = {
    "España": "Madrid",
    "Francia": "Paris",
    "Italia":"Roma",
    "Portugal":"Lisboa",
    "Alemania":"Berlin",
    "Austria":"Viena"
}

capital = input("Introduce una capital")

if capital not in paises.values():
    print(capital, "no está en la lista")
else:
    for pais, ciudad in paises.items() :
        if capital == ciudad:
            print(f"{capital} es la capital de {pais}")