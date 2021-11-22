#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def read_csv(path):
    with open(path, "r") as file:
        lines = file.readlines()
        if not lines:
            return []
        df = []
        for line in lines:
            if line == "\n":
                continue
            df.append(tuple(line.strip().split(",")))
        return df


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
if __name__ == "__main__":
    print(read_csv("example.csv"))
