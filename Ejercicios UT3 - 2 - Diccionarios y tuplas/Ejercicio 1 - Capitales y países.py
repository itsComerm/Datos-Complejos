'''Escribe un programa que almacene en un diccionario las capitales de varios países,
se introducirán los datos con la forma PAIS-CAPITAL. Esto debe ejecutarse indefinidamente hasta que
el usuario introduzca "FIN INSERCIONES". El programa debe permitir al usuario consultar la capital
de un país introduciendo su nombre. Si el país no está en el diccionario, el programa debe informar al usuario.'''

paises = {}

entrada = input("Introduce un país a la lista en formato (PAIS-CAPITAL): ").lower()


while entrada != "FIN".lower():
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais]=capital
    entrada = input("Introduce un país a la lista en formato (PAIS-CAPITAL), para finalizar escribe FIN:").lower()

pais = input("Que país quieres buscar? ")

if pais in paises:
    print(f"El pais {pais}, si se encuentra en la lista y su capita és: {capital}")
else: print(pais, "no se encuentra en la lista.")
