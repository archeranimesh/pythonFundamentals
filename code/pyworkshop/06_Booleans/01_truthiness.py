# Various value which evaluates to true or false.
# We can check the truthiness using bool().

# integers.
print("Number 0's truthiness is: ", bool(0))  # False
print("Number 1's truthiness is: ", bool(1))  # True

# Collections.
# Empty list, dict, tuple, set are False.
print("Empty List truthiness is: ", bool([]))  # False
print("Empty Tuple truthiness is: ", bool(()))  # False
print("Empty Dict truthiness is: ", bool({}))  # False
print("Empty Set truthiness is: ", bool(set()))  # False

# Non empty Collections are True.
print("Single item List truthiness is: ", bool([1]))  # True
print("Single item Tuple truthiness is: ", bool((1,)))  # True
print("Single item Dict truthiness is: ", bool({1: "1"}))  # True
print("Single item Set truthiness is: ", bool({1}))  # True

# String
# Empty String is False, otherwise True
print("Empty String truthiness is: ", bool(""))  # False
print("String truthiness is: ", bool("a"))  # True

# None type is False
print("None type truthiness is: ", bool(None))  # False
