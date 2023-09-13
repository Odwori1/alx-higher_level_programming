#!/usr/bin/python3
"""Imported module for add_item"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """func that get dict, names if only string"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        else:
            return self.__dict__.copy()
