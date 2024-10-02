#!/usr/bin/python3
"""This module defines a class with instance variable"""


class Square:
    """A class that defines a square

    Attributes:
    __size(int): Private instance attribute representing the size of a square

    Methods:
    __init__(self, size): constructor to initialize the size variable
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size(int): The size of the square
        """
        self.__size = size
