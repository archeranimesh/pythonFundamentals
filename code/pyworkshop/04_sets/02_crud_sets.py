colors = {"Red", "Green", "Blue"}

# add(): adds item to the set.
colors.add("Magenta")
print(colors)

# discard(): removes item from set without error if not present.
colors.discard("Blue")
colors.discard("Blue")
print(colors)

# remove(): removes item from set with KeyError if not present.
colors.remove("Red")
# colors.remove("Red")  # KeyError: 'Red'

numbers = {1, 2, 3, 4}

# update(): adds items from a sequence into a set.
colors.update(numbers)
print(colors)

# Below is a string, which will be stored as A, n, d, y
colors.update("Andy")
print(colors)
