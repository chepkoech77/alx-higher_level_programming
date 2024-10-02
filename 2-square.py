#!/usr/bin/python3
"""This module defines a class with private instance"""


class Square:
    """This is a definition of class Square

    Attributes:
        __size(int):private instance of square

    Methods:
        __init__(self, size=0):constructot to initialize tha size variable

    """

    def __init__(self, size=0):
        """This method initializes the size variable

        Args:
            size(int): the size if the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
