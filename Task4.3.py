#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):  # checks if file exists
        return False

    with open(path_reading, "r") as input_file:
        lines = input_file.readlines()
        if not lines:  # checks if input_file is empty, creates empty output file
            with open(path_writing, "w") as output_file:
                return
        else:
            with open(path_writing, "w") as output_file:
                output_file.write("Firstname,Lastname")
                for line in lines:
                    if "Name" in line:
                        continue
                    if line.startswith("\n"):
                        output_file.write("\n,")
                    if ";" in line:
                        semicolon = line.find(";")
                        line = line.replace("\n", "")
                        output_file.write("\n" + line[semicolon + 2:] + "," + line[:semicolon])
                    elif " " in line:
                        line = line.replace(" ", ",")
                        output_file.write("\n" + line[:-1])


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "./my_data.txt"
OUTPUT_PATH = "./my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
