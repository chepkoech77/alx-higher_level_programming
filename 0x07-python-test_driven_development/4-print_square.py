#!/usr/bin/python3
"""This module defines a method that prints a square"""


def print_square(size):
    """This function prints a square
        args:
            size(int): size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print()
