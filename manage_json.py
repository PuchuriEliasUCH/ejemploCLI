import json
import os

data_structure = {
    "users": [],
    "areas": [],
}

def read_json():
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as doc:
            json.dump(data_structure, doc)
    
    with open('data.json', 'r') as doc:
        data = json.load(doc)

    return data

def write_json(data):
    with open('data.json', 'w') as doc:
        json.dump(data, doc)

