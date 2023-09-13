#!/usr/bin/python3
"""The module for to_json_string"""
import json


def to_json_string(my_obj):
    """func that returns the JSON representation

    Args:
        my_obj: the object

    Returns: the JSON representation of an object
    """
    return json.dumps(my_obj)
