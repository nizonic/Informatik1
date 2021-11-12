#!/usr/bin/env python3

# No tests are provided for this task
from unittest import TestCase
from waldo import where_is_waldo

class WaldoTest(TestCase):
    def test_empty(self):
        actual = where_is_waldo([])
        expected = None
        self.assertEqual(actual, expected)
    def test_1(self):
        actual = where_is_waldo(["Bob", "Waldo", "Alice"])
        self.assertEqual(actual, 1)
    def test_2(self):
        actual = where_is_waldo(["Bob", "Waldo", "Waldo"])
        self.assertEqual(actual, 1)
    def test_3(self):
        actual = where_is_waldo(["Waldo", "Waldo", "Waldo"])
        self.assertEqual(actual, 0)
    def test_bad(self):
        actual = where_is_waldo(("Okay", "Let's go", "Waldo"))
        self.assertEqual(actual, 2)
    def test_last(self):
        actual = where_is_waldo(["Weldi", "Woldo", "walad"])
        self.assertEqual(actual, None)
    def test_final(self):
        actual = where_is_waldo(["waldo", "Waldoi"])
        self.assertEqual(actual, None)
