#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    # implement this function
    if a < 0:
        a = -a
    return a


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    # implement this function
    a = absolute_value(a)
    b = absolute_value(b)
    if a == 0 and b == 0:
        return None
    elif a != 0 and b == 0:
        return a
    else:
        return gcd(b, a % b)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
if __name__ == "__main__":
    a = 17
    b = 33
    print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
