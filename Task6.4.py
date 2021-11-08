#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def visualize(records):
    header = list(records).pop(0)
    data = records[1]
    first = 0
    first_alive = 0
    second = 0
    second_alive = 0
    third = 0
    third_alive = 0
    for people in data:
        if people[1] == 1:
            first += 1
            if people[0]:
                first_alive += 1
        elif people[1] == 2:
            second += 1
            if people[0]:
                second_alive += 1
        elif people[1] == 3:
            third += 1
            if people[0]:
                third_alive += 1
    classes = "== {c}st Class =="
    total = "Total |{stars:<20}| {percentage:%}"
    alive = "Alive |{stars:<20}| {percentage:%}"
    total_count = first + second + third
    first_percentage = total_count // first
    second_percentage = total_count // second
    third_percentage = total_count // third
    f_ratio = first_alive / first * 100 // 5
    s_ratio = second_alive / second * 100 // 5
    t_ratio = third_alive / third * 100 // 5
    first_class = classes.format(c=1)
    second_class = classes.format(c=2)
    third_class = classes.format(c=3)
    first_total = total.format(stars=first_percentage // 5 * "*", percentage=first_percentage)
    second_total = total.format(stars=second_percentage // 5 * "*", percentage=second_percentage)
    third_total = total.format(stars=third_percentage // 5 * "*", percentage=third_percentage)
    f_alive = alive.format(stars=int(f_ratio) * "*", percentage=first_alive / first)
    s_alive = alive.format(stars=int(s_ratio) * "*", percentage=second_alive / second)
    t_alive = alive.format(stars=int(t_ratio) * "*", percentage = third_alive / third)
    all = classes.format(c=1) + "\n" + total.format(stars=first_percentage // 5 * "*", percentage=first_percentage) + "\n" + alive.format(stars=int(f_ratio) * "*", percentage=first_alive / first) + "\n" + classes.format(c=2) + "\n" + total.format(stars=second_percentage // 5 * "*", percentage=second_percentage) + "\n" + alive.format(stars=int(s_ratio) * "*", percentage=second_alive / second) + "\n" + classes.format(c=3) + "\n" + total.format(stars=third_percentage // 5 * "*", percentage=third_percentage)  + "\n" + alive.format(stars=int(t_ratio) * "*", percentage = third_alive / third)
    return all


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
    ]
)))
