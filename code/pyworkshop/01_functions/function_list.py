# Making a mutable object (list), as a default argument is a bad idea.
# The list is created on the first call and then same is shared.


def mutable_list(a, b=[]):
    b.append(a)
    print("B is ", b)


mutable_list(3)  # B is  [3]
mutable_list(4)  # B is  [3, 4]

# We should do this.
def new_list(a, b=None):
    if b is None:
        b = []
    b.append(a)
    print("B is  new_list()", b)


new_list(2)  # B is  [2]
new_list(4)  # B is  [4]
new_list(4, [1, 2, 3])  # B is  [1, 2, 3, 4]

# Pythonic Way
def new_list_2(a, b=None):
    b = b or []
    b.append(a)
    print("B is  new_list_2()", b)


new_list_2(2)
new_list_2(4)
new_list_2(4, [1, 2, 3])

