"""
sort / sorted - (key / reverse)
"""


fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
print(fruits)

sorted(fruits, key=len, reverse=True)
print(fruits)

fruits.sort()
