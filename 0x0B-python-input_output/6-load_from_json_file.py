#!/usr/bin/python3
"""module for load_from_json_file"""
import json


def load_from_json_file(filename):
    """func that creates an Object from a “JSON file”

    Args:
        filename: JSON filename
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
