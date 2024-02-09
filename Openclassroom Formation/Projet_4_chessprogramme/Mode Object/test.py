import json

# Données à stocker dans le fichier JSON
data = {
    "name": "John Doe",
    "age": 31,
    "city": "New York"
}

# Écriture des données dans un fichier JSON
with open("example2.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

with open("example.json", "r") as json_file:
    dataR = json.load(json_file)

print(dataR)

