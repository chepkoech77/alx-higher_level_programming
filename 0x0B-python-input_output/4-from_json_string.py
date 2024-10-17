#!/usr/bin/python3
"""This module defines a function"""


import json


def from_json_string(my_str):
    """This is a function definition
    Args:
        my_str:json to deserialize
    """
    return json.loads(my_str)
