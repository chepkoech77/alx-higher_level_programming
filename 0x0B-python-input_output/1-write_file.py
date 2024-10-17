#!/usr/bin/python3
"""This module defines a function"""


def write_file(filename="", text=""):
    """This function writes to a text file"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
