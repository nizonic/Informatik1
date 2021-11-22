#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gender_class_rates(dataset):
    # implement this function
    # the function might have other useful parameters, explore `help(round)`
    header = list(dataset).pop(0)
    data = dataset[1]
    male_values = ["male", "Male", "M", "m"]
    firstm = 0
    firstfm = 0
    secondm = 0
    secondfm = 0
    thirdm = 0
    thirdfm = 0
    for people in data:
        if len(people) != 6:
            return None
        if people[3] in male_values:
            if people[1] == 1:
                firstm += 1
            elif people[1] == 2:
                secondm += 1
            elif people[1] == 3:
                thirdm += 1
        else:
            if people[1] == 1:
                firstfm += 1
            elif people[1] == 2:
                secondfm += 1
            elif people[1] == 3:
                thirdfm += 1

    total_passengers = firstm + firstfm + secondm + secondfm + thirdm + thirdfm
    if firstm != 0:
        ratio_1m = round(firstm / total_passengers * 100, 1)
    else:
        ratio_1m = None
    if secondm != 0:
        ratio_2m = round(secondm / total_passengers * 100, 1)
    else:
        ratio_2m = None
    if thirdm != 0:
        ratio_3m = round(thirdm / total_passengers * 100, 1)
    else:
        ratio_3m = None
    if firstfm != 0:
        ratio_1fm = round(firstfm / total_passengers * 100, 1)
    else:
        ratio_1fm = None
    if secondfm != 0:
        ratio_2fm = round(secondfm / total_passengers * 100, 1)
    else:
        ratio_2fm = None
    if thirdfm != 0:
        ratio_3fm = round(thirdfm / total_passengers * 100, 1)
    else:
        ratio_3fm = None

    return ((ratio_1m, ratio_2m, ratio_3m), (ratio_1fm, ratio_2fm, ratio_3fm))


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!


# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the functions that you have written in Task 1+2.
# The following example is not complete.
if __name__ == "__main__":
    print(gender_class_rates((
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        [
            (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
             'female', 38, 71.2833),
            (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
            # ...
        ]
    )))
