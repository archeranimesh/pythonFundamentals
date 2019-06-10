# Function with no arguments and no return type
def foo():
    print("Hello, World")


# Function with no arguments and a return type
def meaning_of_life():
    return 42


# Function with 2 arguments and a return type
def add_numbers(x, y):
    return x + y


# Function with multi-line function body.
def greeting(name):
    greeting = "Hello "
    return greeting + name  # return is always optional in function.


# Call the Function
foo()

# Function which does not return anything explicitly will return None.
print(type(foo()))

x = meaning_of_life()
print("Meaning of life = ", x)

print("Sum of 5 and 6 is, ", add_numbers(5, 6))

print(greeting("Animesh"))

