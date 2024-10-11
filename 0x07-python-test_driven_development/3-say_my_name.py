#!/usr/bin/python3
"""This module has  function that prints name"""


def say_my_name(first_name, last_name=""):
    """This function prints out the name
        args:
            first_name: first param
            last_name: second param, Defaults to ""
        Raises:
            TypeError: When one or no parameter is passed
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is", first_name)
