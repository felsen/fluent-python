"""
_fields   -> it returns the collection attributes from the class.
_make()   -> instanitate namedtuple from an iterable.
_asdict() -> returns collections of OrderedDict from the namedtuple.
"""


from collections import namedtuple


City = namedtuple("City", "name country population coordinates")
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.name)
print(tokyo.country)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[0])
print(tokyo[1])

print(City._fields)

LatLng = namedtuple("LatLng", "lat, lng")
delhi_data = City("Delhi NCR", "IN", 21.936, LatLng(34.8975, 18.8976))
delhi = City._make(delhi_data)
delhi._asdict()
print(delhi)

for key, value in delhi._asdict().items():
    print("{key}: {value}".format(key=key, value=value))
