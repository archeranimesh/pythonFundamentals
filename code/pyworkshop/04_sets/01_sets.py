# Create empty set, this is the only way.
a = set()
print(type(a))

# {} creates a dict.
print(type({}))

# No duplicates in sets.
names = {"aaaa", "bbbb", "cccc", "aaaa"}
print(type(names))
print(names)

# Sets can be used to remove duplicates from list.
names_list = ["aaaa", "bbbb", "cccc", "aaaa"]
print(set(names_list))

# Set stores only immutable type.
# a = {"a", (1, 2, 3), [1, 2, 3]}  # TypeError: unhashable type: 'list'
print(type(a))

# to check we can use a function called hash()
print(hash("aaaa"))
# print(hash([]))  # TypeError: unhashable type: 'list'

# print(names[0])  # TypeError: 'set' object does not support indexing
