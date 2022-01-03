import json

def write_json(data, filename="names.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

with open("names.json") as json_file:
    data = json.load(json_file)
    temp = data["names"]
    y = {"firstname": "Pam", "lastname": "Beasley"}
    temp.append(y)

write_json(data)
