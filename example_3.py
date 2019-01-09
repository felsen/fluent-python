"""
Cartesian Product (Multiplication)
"""


colors = ["black", "white"]
sizes = ["S", "M", "L"]

tshirts = [(c, s) for c in colors for s in sizes]
print(tshirts)

lax_coordinates = (33.94, -118.40)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '3114258'), ('BRA', '9783647'), ('ESP', '8976546')]

for p in sorted(traveler_ids):
    print("{}/{}".format(p[0], p[1]))

# tuple unpacking
for k, _ in sorted(traveler_ids):
    print("{}".format(k))

a, b, *rest = range(6) # python3
print(a, b, rest) # unpacking all the rest of the elements except first two elements

a, b, *rest = range(3) # python3
print(a, b, rest) # unpacking all the elements except first two elements

a, b, *rest = range(2) # python3
print(a, b, rest) # unpacking all elements, rest of the elements as empty []

metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), #
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))

fmt = "{:15} | {:^10} | {:9.4f}"
for name, cc, pop, (lat, lng) in metro_areas:
    if lng <= 0:
        print(fmt.format(name, lat, lng))



