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

    def test_h_str(self):
        with self.assertRaises(ValueError):
            calculate_factorial("11")

    def test_h_int(self):
        with self.assertRaises(ValueError):
            calculate_factorial(420)

    def test_n_str(self):
        with self.assertRaises(ValueError):
            calculate_factorial("-5")

    def test_n_int(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-9)

    def test_valid_int(self):
        actual = calculate_factorial(9)
        expected = 362880
        self.assertEqual(expected, actual)

    def test_valid_str(self):
        actual = calculate_factorial("9")
        expected = 362880
        self.assertEqual(expected, actual)

    def test_edge(self):
        with self.assertRaises(TypeError):
            calculate_factorial("-5-2")

    def test_zero_int(self):
        actual = calculate_factorial(0)
        expected = 1
        self.assertEqual(expected, actual)

    def test_zero_str(self):
        actual = calculate_factorial("0")
        expected = 1
        self.assertEqual(expected, actual)