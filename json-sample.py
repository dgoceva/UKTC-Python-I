import json

json_file = open('countries.json')
data = json.load(json_file)
# print(data)
print(data[0])
print(data[0]['name'])

for country in data:
    if country['name'][0].upper() == 'B':
        print(country)

for country in data:
    if country['code'][0].upper() == 'B':
        print(json.dumps(country, indent=2))

print(json.dumps(data, sort_keys=True, indent=2))

output = open('countries-out.json', 'w')
json.dump(data, output, indent=2)
