#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def analyze(posts):
    hashtags_count = {}
    hashtags = []
    import string
    valid_keys = string.ascii_letters + string.digits
    concatenation = " ".join(posts)
    indices = [x for x, char in enumerate(concatenation) if char == "#"]
    if indices[-1] == len(concatenation) - 1:
        indices.pop(-1)
    for index in indices:
        if concatenation[index + 1].isalpha():
            i = 1
            while concatenation[index + i] in valid_keys:
                i += 1
            hashtags.append(concatenation[index + 1: index + i])

    for word in hashtags:
        hashtags_count[word] = hashtags.count(word)

    return hashtags_count


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "###a#", "#"]
print(analyze(posts))
