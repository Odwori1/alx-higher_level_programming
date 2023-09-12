#!/usr/bin/python3
"""Write imported module here"""


def lookup(obj):
    """function that returns list of available attr and mthds of an obj

    Args:
        obj: the object wto lookup
    Returns:
        list of available attr and mthds"""
    return dir(obj)
