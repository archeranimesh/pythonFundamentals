# Always name the list/collection ins plural.

# to ways to create empy list.
empty_list_01 = []
empty_list_02 = list()
print("type(empty_list_01): ", type(empty_list_01))
print("type(empty_list_02): ", type(empty_list_02))

# length is a built-in function, which returns the lenght of the collection
names = ["AniB", "Abhi", "Adi"]
print("len(name)", len(names))

# Members can be accessed using index starting at 0.
print("names[0]: ", names[0])
print("names[1]: ", names[1])
print("names[2]: ", names[2])

# Another way to create list.
names = [
    "Anib",
    "Adi",
    "Abhi",  # unlike json, we can have comma at the last element, helps with git diff
]
print("names[0]: ", names[0])
print("names[1]: ", names[1])
print("names[2]: ", names[2])
