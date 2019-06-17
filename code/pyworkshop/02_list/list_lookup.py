# all list lookup's are slow operations as these are linear in nature.
names = ["xxxx", "yyyy", "zzzz", "xxxx"]

# index(value) returns first index of value
print(names.index("yyyy"))  # 1
print(names.index("xxxx"))  # 0
# print(names.index("aaaa"))  # ValueError: 'aaaa' is not in list


print(names.count("yyyy"))  # 1
print(names.count("xxxx"))  # 2
print(names.count("aaaa"))  # 0 Doest not gives valueerror

