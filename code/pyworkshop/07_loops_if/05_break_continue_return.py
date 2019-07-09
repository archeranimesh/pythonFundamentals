# Break, stops the execution of loop and jumps to end of loop.
# Continue, doesn't continue the following loop statement, but jump to start of loop.
names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

for name in names:
    if len(name) != 4:
        continue  # Start new iteration when len is not 4

    print(f"Hello, {name}")
    if name == "Nina":
        break  # Exit from loop when condition is met

print("Done")


# In nested loop, break exit from the loop it is part of
i = 1
j = 1

while i < 10:
    while j < 10:
        print(f"{i} : {j}")
        j += 1
        if j == 4:
            break  # breaks from inner loop
    i += 1

