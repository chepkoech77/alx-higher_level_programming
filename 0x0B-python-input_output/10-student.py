#!/usr/bin/python3
"""This module defines class"""


class Student:
    """This is a definition of a class"""
    def __init__(self, first_name, last_name, age):
        """This is a constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This is a method"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
                }
