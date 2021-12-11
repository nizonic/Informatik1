#!/usr/bin/python3

from data import words
from string import ascii_lowercase


def words_with_length(length):
    return [word for word in words if len(word) == length]


def words_containing_string(s):
    return [word for word in words if word.find(s) > -1]


def words_starting_with_character(c):
    return [word for word in words if word.startswith(c)]


def alphabet():
    return ascii_lowercase


def dictionary():
    return {letter: words_starting_with_character(letter) for letter in ascii_lowercase}


def censored_words(s):
    return ["x" * len(word) if s in word else word for word in words]
