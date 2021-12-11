#!/usr/bin/env python3
from random import choice
class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        s = "0x" + 4 * choice("0123456789ABCDEF")
        return [s] * (self.rows * self.columns)


if __name__ == "__main__":
    g = GameRunner()
    print(g.generate_hex_codes())