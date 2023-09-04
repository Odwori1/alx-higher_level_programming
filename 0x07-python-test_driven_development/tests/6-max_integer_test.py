#!/usr/bin/python3
"""Unittest for function def max_integer(list=[])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a unittest for max_integer([])"""

    def test_empty_list(self):
        """test when list is empty"""
        self.assertIsNone(max_integer([]), None)

    def test_one(self):
        """test siingle element"""
        self.assertEqual(max_integer([20]), 20)

    def test_no_arg(self):
        """this when there is no argument"""
        self.assertEqual(max_integer(), None)

    def test_positive_numbers(self):
        """test for positive numbers"""
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_negative_numbers(self):
        """test for negative numbers"""
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

    def test_mixed_numbers(self):
        """test for bothe positive and negative numbers"""
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)

    def test_begin_max(self):
        """test list starting with max num"""
        self.assertEqual(max_integer([6, 5, 4, 3, 2, 1]), 6)

    def test_end_max(self):
        """test list ending with min num"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_same_element(self):
        """test foe same el in the list"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_floats(self):
        """test floats in the list"""
        self.assertEqual(max_integer([1.0, 10, 0.10, 10.1]), 10.1)

    def test_strings_list(self):
        """test string in the list"""
        self.assertEqual(max_integer(["hi", "bye", "come", "see"]), "see")

    def test_empty_string(self):
        """test for an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_nan(self):
        """when argument has not a number"""
        self.assertEqual(max_integer([1, float("nan"), 8, 9, 20]), 20)

    def test_non_iterable(self):
        """test for non iterable"""
        with self.assertRaises(TypeError):
            max_integer(42)

    def test_send_a_dict(self):
        """this is another unit test for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{4: 2, 4: 2}, {"four": "two"}])

    def test_mixed_types(self):
        """test for mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])


if __name__ == "__main__":
    unittest.main()
