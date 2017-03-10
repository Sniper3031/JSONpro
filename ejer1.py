import json
with open('landings.json') as data_file:
    data = json.load(data_file)

aterrizajes = data["landings"]["landing"]

for aterrizaje in aterrizajes:
    print "* ", aterrizaje["missionname"], "-->", aterrizaje["result"]
    if aterrizaje["result"] != "Success":
        print "    ", aterrizaje["reason"]