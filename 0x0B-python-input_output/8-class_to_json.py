#!/usr/bin/python3
"""Write module here"""


def class_to_json(obj):
    """func that returns the dic desc with simple data structure”

    Args:
        obj: the object

    Returns: the dictionary description
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
