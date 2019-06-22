# Will learn 3 major operation.

rainbow_color = {"Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"}
favourite_color = {"Red", "Green", "Blue", "Black"}

# Union, |, .union()
print(rainbow_color | favourite_color)
print(rainbow_color.union(favourite_color))

# intersection, &, .intersection()
print(rainbow_color & favourite_color)
print(rainbow_color.intersection(favourite_color))

# difference, ^, difference()
print(rainbow_color - favourite_color)
print(rainbow_color.difference(favourite_color))

# symmetric
print(rainbow_color ^ favourite_color)
print(rainbow_color.symmetric_difference(favourite_color))
