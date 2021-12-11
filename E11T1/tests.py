#!/usr/bin/env python3
from unittest import TestCase
from bank_account import BankAccount
from currency_converter import convert

# You need to add missing imports to make the test work!

class PrivateFunctionalTestSuite(TestCase):

    def test_0_convert(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_1_basic_banking(self):
        sut = BankAccount("CHF")
        sut.deposit(100.0, "CHF")
        sut.withdraw(10.0, "EUR")
        actual = sut.get_balance()
        expected = 89.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_2_currency(self):
        with self.assertRaises(Warning) as ctx:
            convert(100, "CHF", "GBR")

    def test_3_currency(self):
        with self.assertRaises(Warning) as ctx:
            convert(100, "GBR", "CHF")

    def test_4_withdraw(self):
        sut = BankAccount()
        sut.deposit(100)
        with self.assertRaises(Warning) as ctx:
            sut.withdraw(100.1)
    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
