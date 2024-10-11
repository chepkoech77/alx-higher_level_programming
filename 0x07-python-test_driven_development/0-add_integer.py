#!/usr/bin/python3
"""This is a module with add function"""


def add_integer(a, b=98):
    """This is a function returns the  addition of two integers a and b
       Floats are typecasted before addition is perfomed

       Raises:
            TypeError: if a or b is not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)

    return a + b
