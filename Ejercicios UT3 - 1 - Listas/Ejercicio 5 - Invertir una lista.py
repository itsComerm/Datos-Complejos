'''Escribe un programa que pida al usuario una lista de números enteros separados por comas
y la invierta. El programa debe imprimir la lista invertida.
'''
print("Invertir lista.")
lista = input("Introduce los numeros enteros separados por comas: ").split(",")

lista.reverse()
lista_invertida = []
for i in range (len(lista)):
   lista_invertida.append(lista[i])


print(lista_invertida)