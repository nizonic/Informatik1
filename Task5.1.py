#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []
    if not a or not b:
        return mergelist
    lena = len(a)
    lenb = len(b)
    if lena >= lenb:
        for x in range(lena):
            if x >= lenb - 1:
                mergelist.append((a[x], b[-1]))
            else:
                mergelist.append((a[x], b[x]))

    if lenb > lena:
        for x in range(lenb):
            if x >= lena - 1:
                mergelist.append((a[-1], b[x]))
            else:
                mergelist.append((a[x], b[x]))
    return mergelist


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

if __name__ == "__main__":
    print(merge([0, 1, 2], [5, 6]))
