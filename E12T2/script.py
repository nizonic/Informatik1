#!/usr/bin/env python3
import random
from random import choice
class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        return ["0x" + choice("0123456789ABCDEF") + choice("0123456789ABCDEF") + choice("0123456789ABCDEF") + choice("0123456789ABCDEF") for x in range(self.columns * self.rows)]


if __name__ == "__main__":
    g = GameRunner()
    print(g.generate_hex_codes())