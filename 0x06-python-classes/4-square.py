#!/usr/bin/python3
"""This module defines the class Square"""


class Square:
    """This is the definition of Square class

    Attributes:
        __size(int): Size of the square

    Methods:
        area(self): returns the area of of square
        size(self): getter method
        size(self, value): setter method

    """
    def __init__(self, size=0):
        """This method initializes the size variable

        Args:
            size(int):size of the square

        Raises:
            TypeError:if the size is not integer
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """This is a getter method

        Returns:
            int: value of size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a setter method

        Args:
            value: value to set to size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """This is a public instance method

        Returns:
            int: value of area of the square

        """
        return self.__size * self.__size
