rainbow = {"Green": "G", "Red": "R", "Blue": "B"}

# default iteration is on keys.
for color in rainbow:
    print(color)

# iterate over both keys and value.
for key, value in rainbow.items():
    print(key, ":", value)

# iterate over only value.
for value in rainbow.values():
    print(value)

# ennumerate with index, and key value
for i, (key, value) in enumerate(rainbow.items()):
    print(i, key, value)

# .items returns a list of tuple, so we can get order.
print(rainbow.items())
print(type(rainbow.items()))
