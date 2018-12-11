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

