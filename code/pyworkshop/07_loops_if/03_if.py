a = True
b = False

# Most simple if statement.
# prints hello, as cond is true
if a:
    print("Hello")

# When condition is false, does not print.
if b:
    print("World")

# If works with truthiness.
list_a = []
if list_a:
    print("empty list")

list_b = [1, 2]
if list_b:
    print("Full list")

# if-else
# condition is false, prints the else case
if b:
    print("b is true")
else:
    print("b is false")

# if-elif-else
if b:
    print(b)
elif a:
    print(a)
else:
    print("else")
