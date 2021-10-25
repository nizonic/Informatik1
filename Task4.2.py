#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None
    grades = []
    with open(path, "r") as file:
        lines = file.readlines()
        if not lines:  # empty file
            return 0.0
        for line in lines:
            line = line.replace(" ", "")
            if line == "\n" or line.startswith("#"):
                continue  # skip this line
            colon = line.index(":")
            grade = line[colon + 1: -1]
            grade = grade.strip()
            if grade:  # check if grade value exists
                grades.append(float(grade))
    return sum(grades) / len(grades)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test.txt many different values on every "Test & Run"!
print(get_average_grade("Task3.4/my_grades.txt"))
