import json
with open('landings.json') as data_file:
    data = json.load(data_file)

aterrizajes = data["landings"]["landing"]

lista1=[]
for aterrizaje in aterrizajes:
    lista1.append(aterrizaje["missionname"])

cad1 = raw_input("Inserte nombre de mision:")


for aterrizaje in aterrizajes:
    if cad1 == aterrizaje["missionname"]:
        print aterrizaje["missionname"], ".", "Rocket: ", aterrizaje["rocketname"]
    elif cad1 not in lista1:
        print "Mision no existe"
        cad1 = raw_input("Inserte nombre de mision:")