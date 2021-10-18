#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    if a < 0:  # implement this function
        a = -a
    return a


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    # implement this function
    if a == 0 and b == 0:
        return None
    elif a == 0:
        return b
    elif b == 0:
        return a
    a = absolute_value(a)
    b = absolute_value(b)

    greatest_divisor_a = []
    greatest_divisor_b = []
    for i in range(a, 0, -1):
        if a % i == 0:
            greatest_divisor_a.append(i)

    for i in range(b, 0, -1):
        if b % i == 0:
            greatest_divisor_b.append(i)

    for divisor in greatest_divisor_a:
        if divisor in greatest_divisor_b:
            return divisor


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 33
b = 11
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
