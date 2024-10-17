#!/usr/bin/python3
"""This module defines a function"""


def read_file(filename=""):
    """This function reads file
    Args:
        filename: file to read
    """
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end="")
