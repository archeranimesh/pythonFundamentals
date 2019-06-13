account = "[Abhi]: "

# Outside scope variable from global scope can be accessed but not modified.
def twitter_info():
    # Scope of variable inside Function is local to function.
    account = "[AniB]: "
    print(f"Inside function account = {account}")  # [AniB]:


print(f"Outside function account = {account}")  # [Abhi]:
twitter_info()


def twitter_info_2():
    # UnboundLocalError: local variable 'account' referenced before assignment
    # if you comment the next line.
    global account
    print(
        f"Inside function account = {account}"
    )  # error because, attempts to print the uninitialized local variable

    # Comment below line to solve the issue
    account = "[AniB]: "


twitter_info_2()
