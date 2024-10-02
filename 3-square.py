#!/usr/bin/python3
"""This module defines a class that calculates the area of a square"""


class Square:
    """This is a definition of a Square class

    Attributes:
        __size(int): the size of the square

    Methods:
        area(self): calculates the area of the square

    """
    def __init__(self, size=0):
        """This method initializes the size variable

        Args:
        size(int): this size of the square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """This is a method that calculates the area of a square

        Returns:
            int(Area if the current square)

        """

        return self.__size * self.__size
