#!/usr/bin/python3
"""This is a definition of a function"""


import json


def load_from_json_file(filename):
    """This is definition of a function
    Args:
        filename: file to load data from
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
