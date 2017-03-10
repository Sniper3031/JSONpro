import json
with open('landings.json') as data_file:
    data = json.load(data_file)

aterrizajes = data["landings"]["landing"]

cad1 = raw_input("Inserte cadena, HELP para ayuda:")

if cad1 == "HELP":
    print "Pulse enter sin datos para mostrar a todos los astronautas"
    print "Introduzca cualquier letra o conjunto de letras para filtrar"
else:
    for aterrizaje in aterrizajes:
        if aterrizaje["manned"] == "Yes":
            for astronaut in aterrizaje["astronaut"]:
                if astronaut.startswith(cad1):
                    print astronaut


