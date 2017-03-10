import json
with open('landings.json') as data_file:
    data = json.load(data_file)

aterrizajes = data["landings"]["landing"]

cont = 0
for aterrizaje in aterrizajes:
    if aterrizaje["manned"] == "Yes":
        cont = cont + 1

print cont