#!/usr/bin/python3
"""This checks inheritance of a class"""


def inherits_from(obj, a_class):
    """Function to check inheritabce
        args:
            obj: object to be checked
            a_class: the class
        Returns:
            boolean: True otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
