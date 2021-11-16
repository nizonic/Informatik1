#!/usr/bin/env python3
from unittest import TestCase
from public.script import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_up(self):
        # NOTE: this test case is buggy and needs fixing!
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        self.assertEqual(expected, actual)

    def test_move_left(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "left")
        expected = (
            (
                "#####   ",
                "###    #",
                "#  o  ##",
                "   #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_down(self):
        state = (
            "#####   ",
            "###    #",
            "#o    ##",
            "   #####"
        )
        actual = move(state, "down")
        expected = (
            (
                "#####   ",
                "###    #",
                "#     ##",
                " o #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_player_count(self):
        state = (
            "#####o  ",
            "###    #",
            "#o    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_no_players(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_lengths(self):
        state = (
            "#####  ",
            "###    #",
            "#o    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_lengths2(self):
        state = (
            "",
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_lengths3(self):
        state = (

        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_valid_chars(self):
        state = (
            "#####O  ",
            "###    #",
            "#o    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_left(self):
        state = (
            "#####   ",
            "###    #",
            "#o    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def right(self):
        state = (
            "#####   ",
            "###    #",
            "#    o##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_down(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_up(self):
        state = (
            "#####   ",
            "###    #",
            "#o    ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")
