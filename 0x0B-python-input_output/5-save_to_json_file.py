#!/usr/bin/python3
"""This module defines a function"""


import json


def save_to_json_file(my_obj, filename):
    """This is the definition of a function
    Args:
        my_obj: object to serialize
        filename: file to write json to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
