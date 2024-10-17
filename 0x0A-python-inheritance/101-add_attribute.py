#!/usr/bin/python3
"""This module defines a function"""


def add_new_attribute(obj, attr_name, attr_value):
    """This function adds new attribute if possible"""
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
