#!/usr/bin/python3
"""This module contains a function to returns attr"""


def lookup(obj):
    """This function returns list of attributes and methods
        args:
            obj(object): param
        Returns:
            list: of attributes and methods
    """
    return(dir(obj))
