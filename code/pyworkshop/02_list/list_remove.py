names = ["xxxx", "yyyy", "zzzz", "xxxx"]

print(names.remove("xxxx"))
print(names)
print(names.remove("xxxx"))  # if element is not present in list it does not throw error

print(names)
print(names.pop())
print(names)

print(names)
print(names.pop())
print(names)

# IndexError: pop from empty list
# print(names.pop())
