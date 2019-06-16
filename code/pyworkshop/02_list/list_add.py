names = ["xxxx", "yyyy", "zzzz"]

print(names)

# append() add an item to end of the list.
names.append("aaaa")
print(names)

# insert at an index.
names.insert(2, "bbbb")
print(names)

# extend() concatenates 2 list.
second_names = ["ssss", "ffff", "gggg"]
names.extend(second_names)
print(names)
