tel = {'Andrea': 4351, 'Gill': 3506}

tel.update({'Ivan': 3483})
print(tel)

print(tel['Andrea'])

keys = tel.keys()
print(keys)

tel.update({'Ivan':4422})
print(tel)

extension = tel.get('Roy')
print(extension)

print(tel.values())

if 'Andrea' in tel:
    print("'Andrea' is present in the dictionary")
else:
    print("'Andrea' is not present in the dictionary")