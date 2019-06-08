# Script for the Corey Schafer VSCode tutorials.

import math
import os
import sys

print(sys.version)
print(sys.executable)

name = input("Your Name: ")
print("Hello, ", name)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Animesh"))
