colors = ["Red", "Green", "Blue"]

# color is a loop variable.
for color in colors:
    print(color)

# Loop variable scope is present outside loop.
print("Outside Loop: ", color)

# range(): returns 1 value at a time in loops
# 3 Variations of range function.
# 1st variation
print(range(5), type(range(5)))  # range(0, 5) <class 'range'>

# 2st variation
# Start(inclusive) and end index(non inclusive)
# use list(range()) to see the list of values
print(range(1, 5), list(range(1, 5)))  # range(1, 5) [1, 2, 3, 4]

# 3rd Variation.
# Provide a step arguments, default = 1
print(range(1, 5, 2), list(range(1, 5)))  # range(1, 5, 2) [1, 2, 3, 4]
