#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ['0779266313', '0789266313', '0792566313', '0792646313', '0792663113', '0792663130', '0792663213', '0792663313', '0792696313', '0796266313']

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    possible_nr = n
    possible_nrs_for_juliet = set()
    for x in range(2, 10):
        for i in range(0, 10):
            if x != 9:
                possible_nrs_for_juliet.add(possible_nr[: x] + str(i) + possible_nr[x:])
                possible_nr = n
            else:
                possible_nrs_for_juliet.add(possible_nr + str(i))
    possible_nrs_for_juliet = list(set(wa_nrs).intersection(possible_nrs_for_juliet))
    possible_nrs_for_juliet.sort()
    return possible_nrs_for_juliet


# For this particular number, the function should find the
# last element in wa_nrs

if __name__ == "__main__":
    print(get_possible_nrs("079266313"))

