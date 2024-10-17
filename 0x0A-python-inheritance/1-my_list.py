#!/usr/bin/python3
"""This the declaration of a class"""


class MyList(list):
    """This is a class which inhertis from list

        Methods:
            print_sorted(public): prints sorted list
    """
    def print_sorted(self):
        """This prints sorted lists"""
        sorted_list = sorted(self)
        print(sorted_list)
