# Two ways to sort a list.

lottery_numbers = [1, 3, 345, 123, 789, 12341]

# 1st method does not modify the original list,
# returns a shallow copy of original list.
print("sorted list: ", sorted(lottery_numbers))

# reverse the list.
print("reverse list: ", sorted(lottery_numbers, reverse=True))


x = sorted(lottery_numbers)  # returns a list.
print("x = ", x, "\ntypeof(x): ", type(x))

# In place list sorting.
lottery_numbers.sort()
print("list sort: ", lottery_numbers)

# reverse
lottery_numbers.reverse()
print("list reverse: ", lottery_numbers)
