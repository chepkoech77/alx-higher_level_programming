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

    def area(self):
        """This method returns the area of rectangle
        Returns:
            int:area of rectangle

        """
        return self.__height * self.__width

    def perimeter(self):
        """This method returns perimeter
        Returns:
            int:perimeter

        """
        result = 0
        if self.__height == 0 or self.__width == 0:
            result = 0
        else:
            result = 2 * (self.__height + self.__width)
        return result

    def __str__(self):
        """This method prints # charcater"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                result += "#" * self.__width + "\n"
            return result[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
