#!/usr/bin/python3
"""This module is a class"""


class LockedClass:
    """This is a class module"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        else:
            self.__dict__[name] = value
