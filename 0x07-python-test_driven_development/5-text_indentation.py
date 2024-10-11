#!/usr/bin/python3
"""This module has a function to print blank line"""


def text_indentation(text):
    """This is a function to print blank line
        args: 
            text(str)
        Raises:
            TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    chars = ['.', '?', ':']
    
    is_split = False

    for char in text:
        print(char, end='')

        if char in chars:
            print("\n", end='')
