#!/usr/bin/env python3

name = "Hans"
age = 37


# generate the greeting sentence
def generate_greeting():
    # You need to change the following line
    greeting = f'Hello {name}, you are {age} years old!'

    # You don't need to change the following line.
    # It simply returns the string created above.
    return greeting

if __name__ == "__main__":
    print(generate_greeting())
