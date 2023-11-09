import json

CheminTypeBain = r""
CheminCycle = r""

# Ouvrir le fichier JSON en lecture
with open(CheminTypeBain, 'r') as fichier:
    # Charger les données JSON
    TypeBain = json.load(fichier)

# Ouvrir le fichier JSON en lecture
with open(CheminCycle, 'r') as fichier:
    # Charger les données JSON
    TypeCycle = json.load(fichier)

ListTest = ["HDL2524", "HDL-202 "]
DicoTest = {}
for i in range(len(ListTest)):
    DicoTest[ListTest[i]]=TypeCycle[ListTest[i]]

#"frf"