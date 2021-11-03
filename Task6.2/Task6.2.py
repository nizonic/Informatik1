#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def preprocess(records):
    male_values = ["male", "Male", "M", "m"]
    survived_values = ["True", "Yes", "yes", "true", "y", "Y", "Survived", "survived", "T", "t", "Alive", "alive"]
    header = records.pop(0)
    clean = []
    for record in records:
        clean_person = []
        if "" in record[:-1] or "undefined" in record[:-1] or "unknown" in record[:-1]:
            continue
        clean_person.append(True) if record[0] in survived_values else clean_person.append(False)
        if 0 < int(record[1]) <= 3:
            clean_person.append(int(record[1]))
        else:
            continue
        clean_person.append(record[2])
        clean_person.append("male") if record[3] in male_values else clean_person.append("female")
        if 0.0 < float(record[4]) <= 100.0:
            clean_person.append(float(record[4]))
        else:
            continue
        if record[-1] == "" or record[-1] == "undefinded" or record[-1] == "unknown":
            clean_person.append(25.0)
        else:
            clean_person.append(float(record[5])) if float(record[5]) > 0.0 else clean_person.append(25.0)
        clean.append(tuple(clean_person))
    return (header, clean)

    # The following part calls the function and prints the return


# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the function that you have written in Task 1.
# The following example is not complete.

titanic = [
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
    ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
    # ...
]

babaui = [
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
    ('Dead', '3', 'Braund Ms. Maria', 'Female', '21', ''),
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta', 'female', '', ''),
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
]
print(preprocess(babaui))
