#!/usr/bin/python3
"""This module defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """This function searches and replaces astring"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
