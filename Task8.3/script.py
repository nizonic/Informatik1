# !/usr/bin/env python3
import random

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    length = random.randint(min_length, max_length)
    s = ""
    for i in range(length):
        char = random.randint(char_start, char_end)
        s += chr(char)
    return s


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):
    from math import factorial
    if inp == None:
        return None

    elif isinstance(inp, str):
        if inp.isnumeric():
            pass
        elif inp.find("-") == 0:
            if inp[1:].find("-") > -1:
                raise TypeError("TypeError: string")
            elif not inp.isnumeric():
                raise TypeError("TypeError: string")
    if isinstance(inp, int):
        if int(inp) < 0:
            raise ValueError("ValueError: number negative")
        if int(inp) > 10:
            raise ValueError("ValueError: number too large")
    return factorial(int(inp))


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def run(trials):
    results = []
    for x in range(trials):
        fuzzie = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            calculate_factorial(fuzzie)
            results.append((0, ""))
        except ValueError as e:
            if str(e) == "ValueError: number negative":
                results.append((1, "ValueError: number negative"))
            else:
                results.append((1, "ValueError: number too large"))
        except:
            results.append((1, "Other error"))

    return results
    # this function should make use of the other two functions
    # for the input of the fuzzer functions use the global variables
    # this is required else the automatic testing is not working


# The following line calls the function run and prints the return
# value to the Console.

if __name__ == "__main__":
    print(run(10))
