# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):
    # implement this function
    if n == 1:
        return "1 is the multiplicative identity"
    for x in range(2, n):
        if n % x == 0:
            t = n // x
            return f"{n} is not a prime number ({x} * {t} = {n})"
    return "%s is prime" % n
    pass


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test.txt many different values on every "Test & Run"!
print(is_prime(1291))
