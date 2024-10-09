#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """This is definion of  a classs
    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle

    methods:
        __init__: initializes width and height
        width(self):getter
        width(self, value): setter
        height(self): gets height
        height(self, value): sets height

    """
    def __init__(self, width=0, height=0):
        """This method initializes width and height

        args:
            width(int): defaults to 0
            height(int): defaults to 0

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This method retrieves the height
        Returns:
            width(int): width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the width to value
        args:
            value(int): value to be set

        Raises:
            TypeError: if value is not an int
            ValueError: if value is < 0

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """This methods gets height
        Returns:
            height(int):height of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the value of height
        args:
            value(int): value to be sett

        Raises:
            TypeError: if value is not integer
            ValueError: if value is < 0

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
