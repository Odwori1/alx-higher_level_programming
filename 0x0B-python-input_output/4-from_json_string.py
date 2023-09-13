#!/usr/bin/python3
"""The module for from_json_string"""
import json


def from_json_string(my_str):
    """func that returns an object from a string

    Args:
        my_str: the string

    Returns: an obj (Python data structure) rep by a JSON string
    """
    return json.loads(my_str)
