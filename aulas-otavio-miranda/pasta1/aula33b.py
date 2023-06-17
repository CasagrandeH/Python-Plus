import json

d1 = {
    'Pessoa 1': {
        'Nome': 'Gustav',
        'idade': 21,
    },
    'Pessoa 2': {
        'Nome': 'Abella',
        'idade': 26,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)