s = "aB:cD"

# perform the transformation
def transform_string():
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.
    front = ""
    back = ""
    s_copy = s
    colon_index = s_copy.find(":")
    front = s_copy[:colon_index]
    back = s_copy[colon_index + 1:]
    front = front.lower()
    back = back.upper()
    s_copy = front + ":" + back
    res = s_copy

    # You don't need to change the following line.
    # It simply returns the string created above.
    return res

