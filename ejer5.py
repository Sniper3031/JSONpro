# -*- coding: utf-8 -*-
import json
with open('landings.json') as data_file:
    data = json.load(data_file)

aterrizajes = data["landings"]["landing"]

lista1=[]
for aterrizaje in aterrizajes:
    lista1.append(aterrizaje["missionname"])

cad1 = raw_input("Inserte mission: ")
while cad1 not in lista1:
    print "Mision no existente, vuelva a intentarlo"
    cad1 = raw_input("Inserte mission: ")

for aterrizaje in aterrizajes:
    if cad1 == aterrizaje["missionname"]:
        print "Nombre de mision: ", aterrizaje["missionname"]
        print "Fecha mission: ", aterrizaje["date"]
        print "Nombre del cohete: ", aterrizaje["rocketname"]
        print "Resultado: ", aterrizaje["result"]
        if not aterrizaje["result"] == "Success":
            print "Razon: ", aterrizaje["reason"]
        print "Tripulada: ", aterrizaje["manned"]
        if aterrizaje["manned"] == "Yes":
            print aterrizaje["astronaut"]
        print "País: ", aterrizaje["country"]
        print "Objetivo: ", aterrizaje["goal"]
        if aterrizaje["result"] == "Success":
            print aterrizaje["info"]