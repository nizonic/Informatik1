#!/usr/bin/env python3
from unittest import TestCase
from script import fine_calculator


# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class FineCalculatorTest(TestCase):
    def test_Area_Type(self):
        actual = fine_calculator(2, 12)
        expected = "Invalid Area Type"
        self.assertEqual(expected, actual)

    def test_Area_Value(self):
        actual = fine_calculator("Urban", 12)
        expected = "Invalid Area Value"
        self.assertEqual(expected, actual)

    def test_Speed_Type(self):
        actual = fine_calculator("motorway", "250")
        expected = "Invalid Speed Type"
        self.assertEqual(expected, actual)

    def test_Speed_Value(self):
        actual = fine_calculator("motorway", -1)
        expected = "Invalid Speed Value"
        self.assertEqual(expected, actual)

    def test_Speed_Limit(self):
        actual = fine_calculator("urban", 50)
        expected = 0
        self.assertEqual(expected, actual)

    def test_Speed_Limit2(self):
        actual = fine_calculator("expressway", 100)
        expected = 0
        self.assertEqual(expected, actual)

    def test_Speed_Limit3(self):
        actual = fine_calculator("motorway", 120)
        expected = 0
        self.assertEqual(expected, actual)

    def test_calculation(self):
        actual = fine_calculator("urban", 250)
        expected = 160000
        self.assertEqual(expected, actual)
    def test_round(self):
        actual = fine_calculator("motorway", 120.999999999999999999999999999999999999999999999999)
        expected = 0
        self.assertEqual(expected, actual)