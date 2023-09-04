#!/usr/bin/python3
"""Write imported module here"""


def say_my_name(first_name, last_name=""):
    """Function that prints, My name is <first name> <last name>

    Args:
        first_name: a string rep first name
        last_name: string rep second name

    Raises:
        TypeError: if either argument is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
