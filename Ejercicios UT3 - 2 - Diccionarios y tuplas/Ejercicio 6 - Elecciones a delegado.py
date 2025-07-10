candidatos = {
    "carlos": 0,
    "alex": 0,
    "david": 0,
    "roger": 0,
}

ganador = ""
votosGanador = 0
print("\nELECCIONES DELEGADO")
print("-------------------------------------------------------")
print("Candidatos:")
print(", ".join(candidatos.keys()))
print("-------------------------------------------------------")

votacion = input("¿A quién quieres votar? (escribe 'FIN VOTACIONES' para terminar): ").lower()

while votacion != "fin votaciones":
    if votacion in candidatos:
        candidatos[votacion] += 1
        print("--------------------------------------------------------------------")
        print("✅ VOTO REGISTRADO")
        print("Resultado actual: ")
        for candidato, votos in candidatos.items():
            print(f"{candidato}: {votos}")
        print("--------------------------------------------------------------------")

        if candidatos[votacion] > votosGanador:
            ganador = votacion
            votosGanador = candidatos[votacion]

        print(f"🟢 Ganador actual: {ganador} con {votosGanador} votos\n")

    else:
        print("\n❌ Candidato no encontrado. Intenta con uno de estos:")
        print(", ".join(candidatos.keys()))

    votacion = input("¿A quién quieres votar? (escribe 'FIN VOTACIONES' para terminar): ").lower()

empatados = [nombre for nombre, votos in candidatos.items() if votos == votosGanador]

print("\nRESULTADO FINAL")
print("-------------------------------------------------------")
for candidato, votos in candidatos.items():
    print(f"{candidato}: {votos} votos")

print("-------------------------------------------------------")
if len(empatados) > 1:
    print(f"🟡 EMPATE entre: {', '.join(empatados)}")
    print(f"🏅 Gana {ganador.upper()} por ser el primero en alcanzar los {votosGanador} votos.")
else:
    print(f"🏆 El nuevo delegado es: {ganador.upper()} con {votosGanador} votos.")
