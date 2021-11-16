#!/usr/bin/env python3
from unittest import TestCase
from script import calculate_factorial


class MyTests(TestCase):
    def test_None(self):
        actual = calculate_factorial(None)
        expected = None
        self.assertEqual(expected, actual)

    def test_string(self):
        actual = calculate_factorial("12,w")
        self.fail(calculate_factorial("12,w"))

    def test_too_high(self):
        with self.assertRaises(ValueError):
            calculate_factorial("11")

    def test_n_value(self):
        with self.assertRaises(ValueError):
            calculate_factorial("-5")

    def test_valid(self):
        actual = calculate_factorial(9)
        expected = 362880
        self.assertEqual(expected, actual)

    def test_edge(self):
        actual = calculate_factorial("-5-2")
        expected = TypeError("TypeError: string")
        with self.assertRaises(TypeError):
            calculate_factorial("-5-2")
