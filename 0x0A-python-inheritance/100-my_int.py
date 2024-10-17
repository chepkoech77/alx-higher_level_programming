#!/usr/bin/python3
"""This is class module"""


class MyInt(int):
    """This is a rebel class"""
    def __eq__(self, other):
        """This is a method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """This is another method"""
        return super().__eq__(other)
