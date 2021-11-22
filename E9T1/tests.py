#!/usr/bin/env python3

from unittest import TestCase
from script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_substring(self):
        f = ProfanityFilter(["tes"], "1234")
        msg = "hello tes"
        actual = f.filter(msg)
        expected = "hello 123"
        self.assertEqual(expected, actual)

    def test_template_extender(self):
        f = ProfanityFilter(["hahayes"], "12")
        msg = "hahayes oke"
        actual = f.filter(msg)
        expected = "1212121 oke"
        self.assertEqual(expected, actual)

    def test_case_insensitive(self):
        f = ProfanityFilter(["haha"], "34")
        msg = "Haha hAhA HAHA haha hahahuhu oke"
        actual = f.filter(msg)
        expected = "3434 3434 3434 3434 3434huhu oke"
        self.assertEqual(expected, actual)

    def test_subword(self):
        f = ProfanityFilter(["ok"], "*%&)")
        msg = "Schokolade OK-Präsident, Oktober Heliokpter"
        actual = f.filter(msg)
        expected = "Sch*%olade *%-Präsident, *%tober Heli*%pter"
        self.assertEqual(expected, actual)

    def test_subword_keys(self):
        f = ProfanityFilter(["ok", "Schokolade"], "123456")
        msg = "Der OK-Präsident isst gerne Schokolade"
        actual = f.filter(msg)
        expected = "Der 12-Präsident isst gerne 1234561234"
        self.assertEqual(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
