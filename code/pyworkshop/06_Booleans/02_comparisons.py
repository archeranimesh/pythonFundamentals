# Comparision Operators.
# <     :       Less Than
# >     :       Greater Than
# <=    :       Less than equal to
# >=    :       Greater than equal to

# Strings.
# Strings are compared on ASCII value,
# So, Capital Letters are less than Small.
print("'A' < 'a' :", "A" < "a")  # True

# Equality.
# It checks if the values are same.
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a == b: ", a == b)  # True

# is 'Identity'
# Same location in Memory
print("a is b", a is b)  # False
print("a is c", a is c)  # True
# check for Not
print("a is not b", a is not b)  # True
