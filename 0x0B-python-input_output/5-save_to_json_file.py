#!/usr/bin/python3
"""The imported module for save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """func that writes an Object to a text file

    Args:
        my_obj: the object
        filename: filename
    """
    with open(filename, "w", encoding="utf=8") as file:
        json.dump(my_obj, file)
