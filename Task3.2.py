pwd = "aaaAA00++"


def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    lowerCharacters = sum(1 for char in pwd if char.islower())
    upperCharacters = sum(1 for char in pwd if char.isupper())
    digits = sum(1 for digit in pwd if digit.isdigit())
    specials = 0
    if 8 <= len(pwd) <= 16 and digits >= 2 and lowerCharacters >= 2 and upperCharacters >= 2:
        for char in pwd:
            if "+" in char or "-" in char or "*" in char or "/" in char:
                specials += 1
        if specials >= 2:
            validity = True
        else:
            validity = False
    else:
        validity = False

    # You don't need to change the following line.
    return validity


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())
