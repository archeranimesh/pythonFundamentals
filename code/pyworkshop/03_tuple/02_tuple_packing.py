student = ("Marcy", 8, "History", 3.5)

# Unpack the above tuple to variables.
name, age, subject, gpa = student
print(f"name = {name}, age = {age}, subject = {subject}, gpa = {gpa}")

# name, age, subject = student  # ValueError: too many values to unpack (expected 3)

# use _ to ignore the value
name, age, subject, _ = student
print(f"name = {name}, age = {age}, subject = {subject}, gpa = {_}")

# tuple help return multiple value from function.
def http_status_code():
    return 200, "OK"


code, name = http_status_code()
print(f"code = {code}, name = {name}")
