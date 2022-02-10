import json

d = dict()
# add/update
d['1'] = 'Ivan Ivanov'
d['2'] = 'Petyr Petrov'
d['3'] = 'Lili Marinowa'
print(d)
# delete
d['1'] = ''
d['1'] = None
print(d)
del d['1']
print(d)
# retrieve
for k, v in d.items():
    print(k, '->', v)
# print(d['1'])
print(d.get('1', None))
print(d.get('1', 'invalid key'))

d.clear()
print(d)
# del d
# print(d)

d = {'1': 'Ivan Ivanov', '2': 'Petyr Petrov', '3': 'Lili Marinowa'}
print(len(d))
print(d.keys())
print(d.values())

print(d.get('2', 'invalid key'))
print(d)
print(d.pop('2', None))
print(d)

# json      <->     Python datatypes
# object    <->     dict
# array     <->     list
# string    <->     str
# numerals  <->     int,float
# null      <->     None
# true      <->     True
# false     <->     False
f = open('europe.json')
countries = json.load(f)
f.close()

# print(country[0])
# print(country[0]['properties']['country'])
for country in countries:
    # print(country)
    # print(country['properties'])
    if country['properties']['country'][0].upper() == 'B':
        print(country['properties'])
    if country['properties']['capital'][0].upper() == 'S':
        print(country['properties'])
