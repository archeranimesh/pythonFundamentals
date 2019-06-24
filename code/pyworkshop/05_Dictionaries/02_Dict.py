nums = {"one": 1, "two": 2, "three": 3}

# add new key/Value pair.
nums["four"] = 4
print(nums)

# There are no duplicate key in Dictionaries.
# If new value is assigned to same key, it will
# Override the old value.
nums["two"] = "2222"
print(nums)  # {'one': 1, 'two': '2222', 'three': 3, 'four': 4}

# Existence of a key in dict.
print("one" in nums)

nums["two"] = 2
print(nums)


# Combine two list.
rainbow = {"Green": "G", "Red": "R", "Blue": "B"}
rainbow.update(nums)
print(rainbow)

# Append value to a list in dict.
color = {"Green": ["Spinich"]}
print(color)
vegetable = color
print(type(vegetable["Green"]))
vegetable["Green"].append("Lettuce")
print(color)

# 3 important functions on Dictionaries
# .keys(): returns special list called dict keys
print(nums.keys())
# .values: returns a special list called dict values
print(nums.values())
# .item: returns a list of tuple, called dict items
print(nums.items())
