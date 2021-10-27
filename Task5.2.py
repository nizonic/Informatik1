#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def analyze(posts):
    hashtags = {}
    for lines in posts:
        for word in lines.split():
            if word.startswith("#"):
                word = word.replace("#", "", 1)
                if word.isalpha():
                    if word not in hashtags:
                        hashtags[word] = 1
                    else:
                        hashtags[word] += 1
                elif word[0].isalpha():
                    for char in word:
                        if not char.isalpha():
                            bad_index = word.index(char)
                            if char == "#" and word[bad_index + 1].isalpha():
                                for char in word[bad_index:]:
                                    if word[:bad_index] not in hashtags:
                                        hashtags[word[:bad_index]] = 1
                                    else:
                                        hashtags[word[:bad_index]] += 1
                            elif word[:bad_index] not in hashtags:
                                hashtags[word[:bad_index]] = 1
                            else:
                                hashtags[word[:bad_index]] += 1

    return hashtags


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #wee#kend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
