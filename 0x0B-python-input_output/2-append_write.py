#!/usr/bin/python3
"""This module defines a function"""


def append_write(filename="", text=""):
    """This function appends text to file"""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
