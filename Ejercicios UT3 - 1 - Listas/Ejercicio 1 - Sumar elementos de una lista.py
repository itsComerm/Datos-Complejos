lista_numeros = input("Escribe una lista de numeros separados por coma:").split(",")
print(lista_numeros)

lista_numeros = list(map(int,lista_numeros))

suma = sum(lista_numeros)

print(suma)