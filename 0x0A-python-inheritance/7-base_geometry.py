#!/usr/bin/python3
"""This module defines class"""


class BaseGeometry:
    """This is a class definition
        methods:
            area: area
    """
    def area(self):
        """This is area method
            Raises:
                exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This method checks parameters
            args:
                name(str): string
                value(int): integer
            Raises:
                TypeError: if value is not int
                ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        return value
