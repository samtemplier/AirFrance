import json
from datetime import datetime, timedelta

CheminTypeBain = r"./Données/Bains.json"
CheminCycle = r"./Données/Cycles.json"

# Ouvrir le fichier JSON en lecture
with open(CheminTypeBain, 'r') as fichier:
    # Charger les données JSON
    TypeBain = json.load(fichier)

# Ouvrir le fichier JSON en lecture
with open(CheminCycle, 'r') as fichier:
    # Charger les données JSON
    TypeCycle = json.load(fichier)

ListTest = ["Cycle_220", "Cycle_60"]

for cycleName in range(len(ListTest)):
    cycle = TypeCycle[ListTest[cycleName]] #définition du cycle
    bainList = cycle["Bain"] #selection des bains
    dureeBain = cycle["Duree"] #selection des durées
    bainUse = TypeBain[bainList[0]] #selection du bain
    timeBain = datetime.strptime(bainUse["Time"], "%H:%M:%S").time()
    stringBain = "00:" + str(dureeBain[0]) + ":00"
    timeCycle = datetime.strptime(stringBain, "%H:%M:%S").time()

    delta1 = timedelta(hours=timeBain.hour, minutes=timeBain.minute)
    delta2 = timedelta(hours=timeCycle.hour, minutes=timeCycle.minute)

    timeBain = delta1 + delta2
    timeInit = datetime.strptime(cycle["Time"], "%H:%M:%S").time()
    delta1 = timedelta(hours=timeInit.hour, minutes=timeInit.minute)
    cycle["Time"] = str(delta1 + delta2)

print(TypeCycle)


    
