def add_numbers(x, y):
    return x + y


# TypeError: add_numbers() missing 1 required positional argument: 'y'
# add_numbers(3)

# Default arguments.
# Always come's last
def say_greetings(name, greeting="Hello"):
    print(f"{greeting} {name}")


# Call with only positional arguments
say_greetings("animesh")

# Call with both
say_greetings("animesh", "Bonjour")

# SyntaxError: non-default argument follows default argument
# Always come's last
"""
def bad_greetings(greeting="Hello", name):
    print(f"{greeting} {name}")
"""


def create_query(language="JavaScript", num_stars=50, sort="desc"):
    print(f"{language}, {num_stars} {sort}")


# None
create_query()  # JavaScript, 50

# one
create_query("Python")  # Python, 50 desc

# All
create_query("Ruby", 50, "desc")  # Ruby, 50 desc


def foo(a, b=5):
    print(f"a = {a}, b = {b}")
    return a + b


print("foo(3) ", foo(3))
print("foo(a = 2, b = 4) ", foo(a=2, b=4))

# Order of calling default arguments are not defined.
print("foo(b = 3, a = 4) ", foo(b=3, a=4))

