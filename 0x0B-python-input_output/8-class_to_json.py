#!/usr/bin/python3
"""This module defines a function"""


def class_to_json(obj):
    """This is a definition of a function
    args:
        obj: instance of  aclass
    """
    if not hasattr(obj, '__dict__'):
        return obj

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
        elif hasattr(value, '__dict__'):
            result[key] = class_to_json(value)
    return result
