# We can get a part of list by using slice.
my_list = ["h", "e", "l", "l", "o", "!"]

print(my_list[0:3])  # Returns 0 - 2nd index
print(my_list[:])  # clone full list
print(my_list[-1])  # Special way to get last element

del my_list[2]  # delete item from list.
print(my_list)
