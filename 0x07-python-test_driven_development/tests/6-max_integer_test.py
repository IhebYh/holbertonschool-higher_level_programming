#!/usr/bin/python3
"""
Unittest for max_integer([])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for max_integer"""
    def test_normal(self):
        """ test normal input"""
        self.assertEqual(max_integer([1, 2, 3, 4], 4))

    def test_no_arg(self):
        """tests empty input"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """tests empty list"""
        self.assertEqual(max_integer([]), None)

    def test_identical(self):
        """test identical input"""
        self.assertEqual(max_integer([1, 1, 1], 1))

    def test_unordered(self):
        """ tests unordered input"""
        self.assertEqual(max_integer([4, 8, 2, 7], 8))

    def test_positive_negative(self):
        """ tests positive/negative input"""
        self.assertEqual(max_integer([-32, 2, -8, 10, -1]), 10)

    def test_negative(self):
        """ tests negative input"""
        self.assertEqual(max_integer([-32, -2, -8, -10, -1]), -1)

    def test_float(self):
        """ tests float input"""
        self.assertEqual(max_integer(
                                    [-32.0001, -32.001,
                                     2.885, -8.058,
                                     10.5569, 1.058]), 10.5569)

    def test_numeric_str(self):
        """ tests positive/negative input"""
        self.assertEqual(max_integer("198565468"), "9")

    def test_string(self):
        self.assertEqual(max_integer("IhebYh", "h"))


if __name__ == "__main__":
    unittest.main()
