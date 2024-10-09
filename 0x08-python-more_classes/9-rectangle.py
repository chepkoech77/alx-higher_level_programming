#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """This is definion of  a classs
    Attributes:
        width(int): private  width of rectangle
        height(int): private height of rectangle
        number_of_instances(int): public
        print_symbol(any): public
    methods:
        __init__: initializes width and height
        width(self):getter
        width(self, value): setter
        height(self): gets height
        height(self, value): sets height
        bigger_or_equal(rect_1, rect_2): static method
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method initializes width and height

        args:
            width(int): defaults to 0
            height(int): defaults to 0

        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This methd compares rectangles
        args:
            rect_1: first rectangle
            rect_2: second rectangle

        Returns:
            (int): biggest rect in area
        Raise:
            TypeError: if either is not an instance of
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
                result += str(self.print_symbol) * self.__width + "\n"
            return result[:-1]

    def __repr__(self):
        """This is a repl"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """This is a class method"""
        return cls(size, size)
