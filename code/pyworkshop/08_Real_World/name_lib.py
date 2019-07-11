# This file will be used as a lib.


def name_in_upper_case(name):
    return name.upper()


if __name__ == "__main__":
    print(name_in_upper_case("Ani"))

    # Prints the name __main__ when invoked as a script.
    # Prints the file name, when invoked as lib
    print(__name__)
