#!/usr/bin/python3
"""Module to chech instance of an object"""


def is_kind_of_class(obj, a_class):
    """This method checks class instance
        args:
            obj(object)
            a_class(class)
        Returns:
            True if it is instance else false
    """
    return isinstance(obj, a_class)
