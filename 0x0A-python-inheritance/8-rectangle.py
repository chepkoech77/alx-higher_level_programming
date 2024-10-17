#!/usr/bin/python3
"""This module defines a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class definition of Rectangle
        Attributes:
            Inherits all attributes from main class

        Methods:
            Inherits all methods from main class
    """

    def __init__(self, width, height):
        """This is a constructor"""
        self.__height = self.integer_validator("height", height)
        self.__width = self.integer_validator("width", width)
