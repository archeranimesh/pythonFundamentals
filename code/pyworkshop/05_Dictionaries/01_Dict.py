# Dictionaries store key:value pair.
# It is mutable.
# the Key is immutable.
# Search is very fast.


# Create empty dict.
a = {}
b = dict()
print(type(a), type(b))

# create a dict.
a = {"one": 1, "two": 2, "three": 3}

# Retrieve the value
# Keys are not ordered.
print(a["one"])  # 1

# get function.
print(a.get("four"))  # if the key is not present does not throw error
# Returns default value if the key is not present.
print(a.get("four", "default value"))
# print(a["four"])  # KeyError: 'four'
