#!/usr/bin/python3
"""This module defines a method"""


def is_same_class(obj, a_class):
    """This function checks for instance of class
        args:
            obj(instance): object
            a_class(class): class
        Returns:
            True if its and instance else false
    """
    return type(obj) is a_class
