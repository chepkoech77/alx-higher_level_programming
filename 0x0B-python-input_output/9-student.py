#!/usr/bin/python3
"""This module defines class"""


class Student:
    """This is a definition of a class"""
    def __init__(self, first_name, last_name, age):
        """This is a constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This is a method"""
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
