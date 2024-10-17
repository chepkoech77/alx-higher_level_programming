#!/usr/bin/python3
"""This module defines a function"""

import json


def to_json_string(my_obj):
    """This is a definition of a method
    Args:
        my_obj: object to serialize
    """
    return json.dumps(my_obj)
