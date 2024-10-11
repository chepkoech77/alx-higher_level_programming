# tests
"""This module defines tests"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class tests the function"""
    def test_empty_list(self):
        # Test empty list
        self.assertIsNone(max_integer([]))
    
    def test_max_positive_numbers(self):
        # Test when all numbers are positive
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_negative_numbers(self):
        # Test when all numbers are negative
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        # Test for positive and negative
        self.assertEqual(max_integer([-1, 2, 4, -3]), 4)

    def test_single_number(self):
        # Test when list is one value
        self.assertEqual(max_integer([5]), 5)

    def test_duplicates(self):
        # Test for duplicates
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_mixed_types(self):
        # Test when list is mixed types
        with self.assertRaises(TypeError):
            max_integer([1, "one", 3])

    def test_with_none(self):
        # Test when list contain None
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2])

    if __name__ == '__main__':
        unittest.main()


