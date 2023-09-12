#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Func that prints list, in sorted (ascending sort)"""
        print(sorted(self))
