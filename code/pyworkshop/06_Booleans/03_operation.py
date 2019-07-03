# 3 booleans operators.
# and, or, not
# The resultant is result is not true or false

a = 2
b = 3
c = 0

print("-" * 30)
# And Table
print(a and b)  # Value of b, 3
print(a and c)  # Value of c, 0
print(c and a)  # Value of c, 0
print(c and c)  # Value of c, 0

print([] and {})  # []
print([1] and {})  # {}
print("-" * 30)

# Or table
print(a or b)  # Value of a, 2
print(a or c)  # Value of a, 2
print(c or a)  # Value of a, 2
print(c or c)  # Value of c, 0

print([] or {})  # {}
print([1] or {})  # [1]

print("-" * 30)

# Not Table
print(not a)  # False
print(not c)  # True

print("1 == True: ", 1 == True)
print("0 == False: ", 0 == False)
